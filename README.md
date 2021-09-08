# cookiecutter-test

![Status](https://badgen.net/badge/status/alpha/d8624d)
![Python Version](https://img.shields.io/pypi/pyversions/cookiecutter-hypermodern-python-instance)
![CalVer](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg)
![License](https://img.shields.io/github/license/cjolowicz/cookiecutter-hypermodern-python)
![Read the Docs](https://img.shields.io/readthedocs/jonzarecki-cookiecutter-test/latest.svg?label=Read%20the%20Docs)
![Tests](https://github.com/jonzarecki/cookiecutter-test/workflows/Tests/badge.svg)
![Codecov](https://codecov.io/gh/jonzarecki/cookiecutter-test/branch/main/graph/badge.svg)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)

DS Cookiecutter template for a Python package based on the
[Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769) article series.

✨📚✨ [Read the full documentation](https://jonzarecki-cookiecutter-test.readthedocs.io/)

## Usage

```bash
$ cruft create https://github.com/jonzarecki/cookiecutter-test
```

## Features

- General automation with [Nox](https://nox.thea.codes/)

- Linting with [pre-commit](https://pre-commit.com/)
- Continuous integration with [GitHub Actions](https://github.com/features/actions)
- Documentation with Sphinx\_ and [Read the Docs](https://readthedocs.org/)
- Automated uploads to [PyPI](https://pypi.org/) and [TestPyPI](https://test.pypi.org/) (TODO)
- Automated release notes with [Release Drafter](https://github.com/release-drafter/release-drafter) (TODO)
- Automated dependency updates with [Dependabot](https://dependabot.com/)
- Code formatting with [Black](https://github.com/psf/black) and [Prettier](https://prettier.io/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Code coverage with [Coverage.py](https://coverage.readthedocs.io/)
- Coverage reporting with [Codecov](https://codecov.io/)
- Static type-checking with [mypy](http://mypy-lang.org/)
- Check documentation examples with [xdoctest](https://github.com/Erotemic/xdoctest)
- Generate API documentation with [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and
  [napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
- Manage project labels with [GitHub Labeler](https://github.com/marketplace/actions/github-labeler)

The template supports Python 3.6, 3.7, 3.8, and 3.9.

## After creation

- create a codecov account (for coverage reporting to work)
- create a readthedocs account (to deploy your documentaiton)

The project doesn't currently support building into a package (might in the future)
