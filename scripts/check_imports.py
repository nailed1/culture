#!/usr/bin/env python3
"""Check that all third-party imports in src/ are declared in requirements.txt."""
import ast
import sys
from pathlib import Path

# Mapping from import name to PyPI package name where they differ
IMPORT_TO_PACKAGE: dict[str, str] = {
    "sklearn": "scikit-learn",
    "cv2": "opencv-python",
    "PIL": "Pillow",
    "bs4": "beautifulsoup4",
    "yaml": "PyYAML",
    "dateutil": "python-dateutil",
    "dotenv": "python-dotenv",
    "jose": "python-jose",
    "pkg_resources": "setuptools",
}

try:
    STDLIB: set[str] = sys.stdlib_module_names  # Python 3.10+
except AttributeError:
    import sysconfig, os

    STDLIB = set()
    stdlib_path = sysconfig.get_paths()["stdlib"]
    for entry in os.listdir(stdlib_path):
        STDLIB.add(entry.split(".")[0])


def collect_imports(src_dir: Path) -> set[str]:
    imports: set[str] = set()
    for py_file in src_dir.rglob("*.py"):
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.level == 0:
                    imports.add(node.module.split(".")[0])
    return imports


def parse_requirements(req_file: Path) -> set[str]:
    packages: set[str] = set()
    for line in req_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        # strip version specifiers and extras
        name = line.split(";")[0].split("[")[0]
        for op in (">=", "<=", "!=", "~=", "==", ">", "<"):
            name = name.split(op)[0]
        packages.add(name.strip().lower())
    return packages


def main() -> None:
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <src_dir> <requirements_file>")
        sys.exit(1)

    src_dir = Path(sys.argv[1])
    req_file = Path(sys.argv[2])

    if not src_dir.exists():
        print(f"Error: directory '{src_dir}' not found")
        sys.exit(1)
    if not req_file.exists():
        print(f"Error: requirements file '{req_file}' not found")
        sys.exit(1)

    raw_imports = collect_imports(src_dir)

    # keep only third-party names (not stdlib, not builtins, not local)
    third_party = {
        imp
        for imp in raw_imports
        if imp not in STDLIB and imp not in sys.builtin_module_names and imp
    }

    # normalize import name → package name
    normalized = {IMPORT_TO_PACKAGE.get(imp, imp).lower() for imp in third_party}

    declared = parse_requirements(req_file)

    missing = normalized - declared
    extra = declared - normalized

    if missing:
        print(f"MISSING from {req_file}:")
        for pkg in sorted(missing):
            print(f"  - {pkg}")

    if extra:
        print(f"EXTRA in {req_file} (not found in imports):")
        for pkg in sorted(extra):
            print(f"  - {pkg}")

    if missing:
        sys.exit(1)

    print(f"OK: all {len(normalized)} third-party import(s) are declared in {req_file}")


if __name__ == "__main__":
    main()
