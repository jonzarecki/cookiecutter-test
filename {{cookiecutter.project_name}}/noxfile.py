"""Nox sessions."""
import shutil
from pathlib import Path

import nox
from nox import Session

package = "ground_scanner"
python_versions = ["3.7"]
nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "tests",
    "xdoctest",
    "docs-build",
)


@nox.session(python=False)
def tests(sess: Session) -> None:
    """Run the test suite."""
    sess.install("coverage[toml]", "pytest", "pygments")
    try:
        sess.run("coverage", "run", "--parallel", "-m", "pytest", *sess.posargs)
    finally:
        sess.notify("coverage", posargs=[])


@nox.session(python=python_versions)
def coverage(sess: Session) -> None:
    """Produce the coverage report."""
    args = sess.posargs or ["report"]

    sess.install("coverage[toml]")

    if not sess.posargs and any(Path().glob(".cache/.coverage.*")):
        # keep .coverage.* files if not interactive (i.e. CI)
        sess.run(*(["coverage", "combine"] + (["--keep"] if not sess.interactive else [])))
    sess.run("coverage", *args)


@nox.session(python=False)
def typeguard(sess: Session) -> None:
    """Runtime type checking using Typeguard."""
    sess.install("pytest", "typeguard", "pygments")
    sess.run("pytest", f"--typeguard-packages={package}", *sess.posargs)


@nox.session(python=False)
def xdoctest(sess: Session) -> None:
    """Run examples with xdoctest."""
    args = sess.posargs or ["all"]
    sess.install("xdoctest[colors]")
    sess.run("python", "-m", "xdoctest", package, *args)


@nox.session(name="docs-build", python=python_versions)
def docs_build(sess: Session) -> None:
    """Build the documentation."""
    args = sess.posargs or ["docs", "docs/_build"]
    sess.install("sphinx", "sphinx-click", "sphinx-rtd-theme")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    sess.run("sphinx-build", *args)


@nox.session(python=python_versions)
def docs(sess: Session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    args = sess.posargs or ["--open-browser", "docs", "docs/_build"]
    sess.install("sphinx", "sphinx-autobuild", "sphinx-click", "sphinx-rtd-theme")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    sess.run("sphinx-autobuild", *args)
