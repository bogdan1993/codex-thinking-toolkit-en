import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base / "source with spaces"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.dest = self.base / "skills destination"
        spec = importlib.util.spec_from_file_location("toolkit_installer", self.repo / "install.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def cli(self, *args, env=None):
        return subprocess.run([sys.executable, "-B", str(self.repo / "install.py"), *args], cwd=self.base, env=env, capture_output=True, text=True)

    def test_dry_run_does_not_create_destination(self):
        result = self.cli("--check", "--dest", str(self.dest))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.dest.exists())

    def test_full_install_preserves_unicode_and_files(self):
        total, count, _ = self.mod.install(self.dest)
        self.assertEqual((total, count), (20, 20))
        self.assertEqual({p.name for p in self.dest.iterdir()}, set(self.mod.package()))
        for name in self.mod.package():
            self.assertEqual(self.mod.inventory(self.repo / "skills" / name), self.mod.inventory(self.dest / name))

    def test_idempotent_install_keeps_mtime(self):
        self.mod.install(self.dest)
        path = self.dest / "analyze" / "SKILL.md"
        before = path.stat().st_mtime_ns
        self.assertEqual(self.mod.install(self.dest)[1], 0)
        self.assertEqual(path.stat().st_mtime_ns, before)

    def test_conflict_preflight_writes_nothing(self):
        target = self.dest / "brand"
        target.mkdir(parents=True)
        original = "Existing user's own brand skill.\n"
        (target / "SKILL.md").write_text(original)
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertEqual(list(self.dest.iterdir()), [target])
        self.assertEqual((target / "SKILL.md").read_text(), original)

    def test_identical_skills_and_unrelated_skills_are_preserved(self):
        shutil.copytree(self.repo / "skills" / "analyze", self.dest / "analyze")
        other = self.dest / "my-unrelated-skill"
        other.mkdir()
        (other / "SKILL.md").write_text("unrelated")
        self.assertEqual(self.mod.install(self.dest)[1], 19)
        self.assertEqual((other / "SKILL.md").read_text(), "unrelated")

    def test_modified_source_is_rejected(self):
        path = self.repo / "skills" / "verify" / "SKILL.md"
        path.write_text(path.read_text() + "Changed")
        result = self.cli("--dest", str(self.dest))
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.dest.exists())

    def test_unlisted_source_is_rejected(self):
        (self.repo / "skills" / "verify" / "unlisted.txt").write_text("unlisted")
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertFalse(self.dest.exists())

    def test_missing_source_is_rejected(self):
        (self.repo / "skills" / "verify" / "LICENSE").unlink()
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertFalse(self.dest.exists())

    def test_manifest_path_escape_is_rejected(self):
        p = self.repo / "manifest.json"
        data = json.loads(p.read_text())
        data["files"]["../outside.txt"] = "0" * 64
        p.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertFalse(self.dest.exists())

    def test_duplicate_skill_names_are_rejected(self):
        p = self.repo / "manifest.json"
        data = json.loads(p.read_text())
        data["skills"].append(data["skills"][0])
        p.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertFalse(self.dest.exists())

    def test_failed_copy_rolls_back_new_directories_only(self):
        shutil.copytree(self.repo / "skills" / "analyze", self.dest / "analyze")
        actual = self.mod.shutil.copytree
        calls = 0
        def copy(source, target, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                (target / "partial.txt").write_text("partial")
                raise OSError("Simulated disk error")
            return actual(source, target, **kwargs)
        with mock.patch.object(self.mod.shutil, "copytree", side_effect=copy):
            with self.assertRaises(OSError):
                self.mod.install(self.dest)
        self.assertEqual([p.name for p in self.dest.iterdir()], ["analyze"])
        self.assertEqual(self.mod.inventory(self.dest / "analyze"), self.mod.inventory(self.repo / "skills" / "analyze"))

    def test_file_in_place_of_skill_is_rejected(self):
        self.dest.mkdir()
        path = self.dest / "verify"
        path.write_text("existing file")
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertEqual(path.read_text(), "existing file")
        self.assertEqual(len(list(self.dest.iterdir())), 1)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_destination_symlink_is_rejected(self):
        self.dest.mkdir()
        try:
            (self.dest / "analyze").symlink_to(self.repo / "skills" / "analyze", target_is_directory=True)
        except OSError as error:
            self.skipTest(str(error))
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertTrue((self.dest / "analyze").is_symlink())

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_nested_destination_symlink_is_rejected(self):
        shutil.copytree(self.repo / "skills" / "analyze", self.dest / "analyze")
        path = self.dest / "analyze" / "SKILL.md"
        path.unlink()
        try:
            path.symlink_to(self.repo / "skills" / "analyze" / "SKILL.md")
        except OSError as error:
            self.skipTest(str(error))
        with self.assertRaises(ValueError):
            self.mod.install(self.dest)
        self.assertEqual(len(list(self.dest.iterdir())), 1)

    def test_codex_home_default_and_cli_from_other_directory(self):
        env = dict(os.environ, CODEX_HOME=str(self.base / "codex-home"))
        result = self.cli(env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.base / "codex-home" / "skills" / "verify" / "SKILL.md").is_file())

    def test_python_cache_does_not_cause_conflict(self):
        self.mod.install(self.dest)
        cache = self.dest / "verify" / "__pycache__"
        cache.mkdir()
        (cache / "cache.pyc").write_bytes(b"cache")
        self.assertEqual(self.mod.install(self.dest)[1], 0)

if __name__ == "__main__":
    unittest.main()
