=================
cookiecutter-test
=================

.. badges-begin

| |Status| |Read the Docs| |Tests| |Codecov|
| |pre-commit| |Black|

.. |Status| image:: https://badgen.net/badge/status/alpha/d8624d
   :target: https://badgen.net/badge/status/alpha/d8624d
   :alt: Project Status
.. |Read the Docs| image:: https://img.shields.io/readthedocs/jonzarecki-cookiecutter-test/latest.svg?label=Read%20the%20Docs
   :target: https://jonzarecki-cookiecutter-test.readthedocs.io/
   :alt: Read the documentation at https://jonzarecki-cookiecutter-test.readthedocs.io/
.. |Tests| image:: https://github.com/jonzarecki/cookiecutter-test/workflows/Tests/badge.svg
   :target: https://github.com/jonzarecki/cookiecutter-test/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/jonzarecki/cookiecutter-test-instance/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/jonzarecki/cookiecutter-test-instance/branch/main/graph/badge.svg
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

.. badges-end

|

.. raw:: html

   <p align="center"><img alt="logo" src="docs/_static/logo.png" width="50%" /></p>


Cookiecutter_ template for a Python package based on the
`Hypermodern Python`_ article series.

✨📚✨ `Read the full documentation`__

__ https://jonzarecki-cookiecutter-test.readthedocs.io/


Usage
=====

.. code:: console

   $ cruft create https://github.com/jonzarecki/cookiecutter-test


Features
========

.. features-begin

- General automation with Nox_
- Linting with pre-commit_
- Continuous integration with `GitHub Actions`_
- Documentation with Sphinx_ and `Read the Docs`_
- Automated uploads to PyPI_ and TestPyPI_ (TODO)
- Automated release notes with `Release Drafter`_ (TODO)
- Automated dependency updates with Dependabot_
- Code formatting with Black_ and Prettier_
- Testing with pytest_
- Code coverage with `Coverage.py`_
- Coverage reporting with Codecov_
- Static type-checking with mypy_
- Check documentation examples with xdoctest_
- Generate API documentation with autodoc_ and napoleon_
- Manage project labels with `GitHub Labeler`_

The template supports Python 3.6, 3.7, 3.8, and 3.9.

After creation:
---------------
- create a codecov account (for coverage reporting to work)
- create a readthedocs account (to deploy your documentation)


The project doesn't currently support building into a package (might in the future)

.. features-end

.. references-begin

.. _Black: https://github.com/psf/black
.. _Codecov: https://codecov.io/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Coverage.py: https://coverage.readthedocs.io/
.. _Dependabot: https://dependabot.com/
.. _GitHub Actions: https://github.com/features/actions
.. _Hypermodern Python: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _Nox: https://nox.thea.codes/
.. _Prettier: https://prettier.io/
.. _PyPI: https://pypi.org/
.. _Read the Docs: https://readthedocs.org/
.. _Release Drafter: https://github.com/release-drafter/release-drafter
.. _Sphinx: http://www.sphinx-doc.org/
.. _TestPyPI: https://test.pypi.org/
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _mypy: http://mypy-lang.org/
.. _napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/latest/
.. _sphinx-click: https://sphinx-click.readthedocs.io/
.. _xdoctest: https://github.com/Erotemic/xdoctest
.. _GitHub Labeler: https://github.com/marketplace/actions/github-labeler

.. references-end
