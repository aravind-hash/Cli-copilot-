from pathlib import Path


def test_repository_files_exist():
    repo_root = Path(__file__).resolve().parents[1]
    assert (repo_root / "README.md").exists()
    assert (repo_root / ".github" / "workflows" / "python-package.yml").exists()
