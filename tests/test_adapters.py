import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]

class AdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('adapters_builder', ROOT/'build_adapters.py')
        cls.builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.builder)
        cls.meta = json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
        cls.names = cls.meta['skills']
        cls.instagram = all(n.startswith('ig-') for n in cls.names)

    def test_generated_files_match_canonical_sources(self):
        expected = self.builder.generate(ROOT)
        actual = {p.relative_to(ROOT/'adapters').as_posix():p.read_bytes() for p in (ROOT/'adapters').rglob('*') if p.is_file()}
        self.assertEqual(expected, actual)
        self.assertEqual(expected, self.builder.generate(ROOT))

    def test_cloud_zip_contains_exact_upload_files(self):
        folder = ROOT/'adapters/chatgpt'
        zips = list(folder.glob('*-chatgpt.zip'))
        self.assertEqual(len(zips), 1)
        with zipfile.ZipFile(zips[0]) as z:
            actual = {n:z.read(n) for n in z.namelist()}
        expected = {p.name:p.read_bytes() for p in folder.iterdir() if p.is_file() and p!=zips[0]}
        self.assertEqual(actual, expected)
        self.assertIn('PROJECT_INSTRUCTIONS.md', actual)
        self.assertIn('COMMANDS.md', actual)
        self.assertEqual(actual['LICENSE'], (ROOT/'LICENSE').read_bytes())

    def test_instruction_size_and_library_coverage(self):
        folder = ROOT/'adapters/chatgpt'
        instructions = (folder/'PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
        self.assertLess(len(instructions), 8000)
        commands = (folder/'COMMANDS.md').read_text(encoding='utf-8')
        headings = re.findall(r'^# /([A-Z][A-Z0-9-]+)$', commands, re.M)
        self.assertEqual(headings, [n.upper() for n in self.names])
        for name,body in self.builder.modes(ROOT,self.names).items():
            self.assertIn(body, commands)

    def test_generated_uploads_exclude_private_paths(self):
        for path,data in self.builder.generate(ROOT).items():
            if path.endswith('.md'):
                value=data.decode('utf-8')
                self.assertNotIn('/Users/',value,path)
                self.assertNotIn('Codex-Skill-Audit',value,path)
                self.assertNotIn('PERSONAL_WRITING_DNA',value,path)

    def test_claude_single_root_archive_and_resolved_references(self):
        if self.instagram:
            self.skipTest('Claude adaptation not requested for Instagram')
        label='thinking-toolkit-'+self.meta['language']
        with zipfile.ZipFile(ROOT/f'adapters/claude/{label}.zip') as z:
            actual={n:z.read(n) for n in z.namelist()}
        base=ROOT/'adapters/claude'
        expected={p.relative_to(base).as_posix():p.read_bytes() for p in (base/label).rglob('*') if p.is_file()}
        self.assertEqual(actual,expected)
        entry=actual[f'{label}/SKILL.md'].decode('utf-8')
        links=re.findall(r'\]\((references/[^)]+)\)',entry)
        self.assertEqual(len(links),20)
        for link in links:
            self.assertIn(f'{label}/{link}',actual)
        self.assertEqual(set(n.split('/')[0] for n in actual),{label})

    def test_check_command_writes_nothing(self):
        paths=list((ROOT/'adapters').rglob('*'))
        before={str(p):p.stat().st_mtime_ns for p in paths if p.is_file()}
        result=subprocess.run([sys.executable,'-B',str(ROOT/'build_adapters.py'),'--check'],capture_output=True,text=True,cwd=ROOT.parent)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(before,{str(p):p.stat().st_mtime_ns for p in paths if p.is_file()})

    def test_instagram_helpers_run_after_extraction(self):
        if not self.instagram:
            self.skipTest('No executable helpers in thinking toolkit')
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(ROOT/'adapters/chatgpt/helpers.zip') as z:
                z.extractall(tmp)
            result=subprocess.run([sys.executable,'-B',str(Path(tmp)/'skills/ig-reel/hookscore.py'),'--hook','Nu mai aștepta promovarea ca să fii lider.','--json'],capture_output=True,text=True,cwd=tmp)
            self.assertIn(result.returncode,(0,1),result.stderr)
            score=json.loads(result.stdout)
            self.assertTrue(score)
            script=Path(tmp)/'script.txt'
            script.write_text('Un proiect blocat poate începe cu o conversație.\n',encoding='utf-8')
            result=subprocess.run([sys.executable,'-B',str(Path(tmp)/'skills/ig-reel/beats.py'),str(script),'--target','30','--wpm','165','--json'],capture_output=True,text=True,cwd=tmp)
            self.assertIn(result.returncode,(0,1),result.stderr)
            self.assertTrue(json.loads(result.stdout))

if __name__=='__main__':
    unittest.main()
