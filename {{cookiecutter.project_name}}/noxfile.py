"""Nox sessions."""
import os
import shutil
from pathlib import Path
from typing import List

import nox
import toml
from nox import Session

package = "{{cookiecutter.package_name}}"
python_versions = ["3.10"]
nox.needs_version = ">= 2021.6.6"
nox.options.sessions = ("tests", "xdoctest", "docs-build")
pyproject_data = toml.loads(Path("pyproject.toml").read_text())
submodule_paths = []
if os.path.exists(".gitmodules"):
    with open(".gitmodules") as f:
        lines = [s.strip() for s in f.readlines()]
    if "path = common" in lines:  # common is not a submodule of a different repo
        submodule_paths.append("common")


@nox.session(python=False)
def tests(sess: Session) -> None:
    """Run the test suite."""
    sess.run("pip", "install", "coverage[toml]", "pytest", "pygments")

    def add_quotes_and_join(lst: List[str]) -> str:
        return ",".join([f"{s}" for s in lst])

    omit_paths = ["--omit"] + [
        add_quotes_and_join(pyproject_data["tool"]["coverage"]["run"]["omit"] + [f"{p}/**" for p in submodule_paths])
    ]
    run_paths = [p for p in pyproject_data["tool"]["coverage"]["run"]["source"] if p not in submodule_paths]

    try:
        sess.run("coverage", "run", "--parallel", *omit_paths, "-m", "pytest", *run_paths, *sess.posargs)
    finally:
        sess.notify("coverage", posargs=[])


@nox.session(python=python_versions)
def coverage(sess: Session) -> None:
    """Produce the coverage report."""
    args = sess.posargs or ["report"]

    sess.run("pip", "install", "coverage[toml]")

    if not sess.posargs and any(Path().glob(".cache/.coverage.*")):
        # keep .coverage.* files if not interactive (i.e. CI)
        sess.run(*(["coverage", "combine"] + (["--keep"] if not sess.interactive else [])))
    sess.run("coverage", *args)


@nox.session(python=False)
def xdoctest(sess: Session) -> None:
    """Run examples with xdoctest."""
    args = sess.posargs or ["all"]
    sess.run("pip", "install", "xdoctest[colors]")
    sess.run("python", "-m", "xdoctest", package, *args)


@nox.session(name="docs-build", python=python_versions)
def docs_build(sess: Session) -> None:
    """Build the documentation."""
    args = sess.posargs or ["docs/source", "docs/_build"]
    sess.run("pip", "install", "-r", "docs/source/requirements.txt")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    sess.run("sphinx-build", *args)


@nox.session(python=python_versions)
def docs(sess: Session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    args = sess.posargs or ["--open-browser", "docs/source", "docs/_build"]
    sess.run("pip", "install", "-r", "docs/source/requirements.txt")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    sess.run("sphinx-autobuild", *args)
