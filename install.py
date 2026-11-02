#!/usr/bin/env python3
"""Install the toolkit without replacing different existing skills (Python 3.10+)."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inventory(root):
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"Expected a real directory: {root}")
    result = {}
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symbolic links are not supported: {path}")
        if "__pycache__" in path.relative_to(root).parts:
            continue
        if path.is_file():
            result[path.relative_to(root).as_posix()] = digest(path)
    return result

def package():
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    names = manifest["skills"]
    if manifest.get("schemaVersion") != 1 or not names or len(set(names)) != len(names):
        raise ValueError("Invalid manifest schema or duplicate skill names")
    if any(not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) for name in names):
        raise ValueError("Invalid skill name")
    expected = manifest["files"]
    for relative in expected:
        path = PurePosixPath(relative)
        if path.is_absolute() or ".." in path.parts or "\\" in relative or str(path) != relative:
            raise ValueError(f"Invalid package path: {relative}")
    found = inventory(ROOT / "skills")
    found = {"skills/" + key: value for key, value in found.items()}
    if found != expected:
        raise ValueError("Skill package differs from manifest (missing, added or modified files)")
    if sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir()) != sorted(names):
        raise ValueError("Skill directories differ from manifest")
    for name in names:
        if f"skills/{name}/SKILL.md" not in expected:
            raise ValueError(f"Missing entrypoint: {name}")
    return names

def install(dest, check=False):
    names = package()
    dest = dest.expanduser().resolve()
    pending = []
    for name in names:
        source, target = ROOT / "skills" / name, dest / name
        if target.exists() or target.is_symlink():
            if inventory(source) != inventory(target):
                raise ValueError(f"Existing different skill; no changes made: {target}")
        else:
            pending.append((source, target))
    if check:
        return len(names), len(pending), dest
    created = []
    try:
        if pending:
            dest.mkdir(parents=True, exist_ok=True)
        for source, target in pending:
            target.mkdir()  # Exclusive ownership; never roll back someone else's directory.
            created.append(target)
            shutil.copytree(source, target, dirs_exist_ok=True)
            if inventory(source) != inventory(target):
                raise RuntimeError(f"Installed content differs: {target}")
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    return len(names), len(pending), dest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "skills"
    parser.add_argument("--dest", type=Path, default=default)
    parser.add_argument("--check", action="store_true", help="Verify sources and destination without writing")
    args = parser.parse_args()
    try:
        total, count, dest = install(args.dest, args.check)
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as error:
        parser.exit(1, f"Error: {error}\n")
    if args.check:
        print(f"Verified {total} skills; {count} to install at {dest}; no conflicts. No files written.")
    else:
        print(f"Installed {count} skills; {total-count} already identical. Destination: {dest}")
        print("Invoke a skill with $analyze, $verify or its other native name. Refresh discovery if needed.")

if __name__ == "__main__":
    main()
