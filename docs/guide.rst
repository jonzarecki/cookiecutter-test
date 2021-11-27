User Guide
==========

This is the user guide
for the `Hypermodern Python Cookiecutter`_,
a Python template based on the `Hypermodern Python`_ article series.

If you're in a hurry, check out the :doc:`quickstart guide <quickstart>`
and the :ref:`tutorials <Tutorials>`.

.. contents::
    :local:
    :backlinks: none


Introduction
~~~~~~~~~~~~

About this project
------------------

The |HPC| is a general-purpose template for Python libraries and applications,
released under the `MIT license`_
and hosted on `GitHub <Hypermodern Python Cookiecutter_>`__.

The main objective of this project template is to
enable current best practices
through modern Python tooling.
Our goals are to:

- focus on simplicity and minimalism,
- promote code quality through automation, and
- provide reliable and repeatable processes,

all the way from local testing to publishing releases.

Projects are created from the template using Cookiecutter_,
a project scaffolding tool built on top of the Jinja_ template engine.

The project template is centered around the following tools:

- Nox_ for automation of checks and other development tasks
- `GitHub Actions`_ for continuous integration and delivery


.. _Features:

Features
--------

Here is a detailed list of features for this Python template:

.. include:: ../README.rst
   :start-after: features-begin
   :end-before: features-end


Release cadence
---------------

The |HPC| has a monthly release cadence while in alpha status.
Releases happen on the 15th of every month.
We use `Calendar Versioning`_ with a ``YYYY.MM.DD`` versioning scheme.

The current stable release is `2021.7.15`_.

.. _2021.7.15: https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases/tag/2021.7.15


.. _Installation:

Installation
~~~~~~~~~~~~

System requirements
-------------------

You need a recent Linux, Unix, or Mac system with
bash_, curl_, and git_.

On Windows 10, enable the `Windows Subsystem for Linux`_ (WSL) and
install the Ubuntu 20.04 LTS distribution.
Open Ubuntu from the Start Menu, and
install additional packages using the following commands:

.. _Windows Subsystem for Linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10

.. code:: console

   $ sudo apt update
   $ sudo apt install -y build-essential curl git libbz2-dev \
     libffi-dev liblzma-dev libncurses5-dev libncursesw5-dev \
     libreadline-dev libsqlite3-dev libssl-dev llvm make \
     python-openssl tk-dev wget xz-utils zlib1g-dev

The project template should also work natively on Windows.
Pull requests to document Windows specifics are welcome!

.. note::

   When working with this template on Windows,
   configure your text editor or IDE
   to use only `UNIX-style line endings`__ (line feeds).

   __ https://en.wikipedia.org/wiki/Newline

   The project template contains a `.gitattributes`_ file
   which enables end-of-line normalization for your entire working tree.
   Additionally, the Prettier_ code formatter converts line endings to line feeds.
   Windows-style line endings (`CRLF`) should therefore never make it into your Git repository.

   .. _.gitattributes: https://git-scm.com/book/en/Customizing-Git-Git-Attributes

   Nonetheless, configuring your editor for line feeds is recommended
   to avoid complaints from the pre-commit_ hook for Prettier.


Getting Python
--------------

It is recommended to use pyenv_ for
installing and managing Python versions.
Please refer to the documentation of this project
for detailed installation and usage instructions.

Install pyenv_ like this:

.. code:: console

   $ curl https://pyenv.run | bash

Add the following lines to your ``~/.bashrc``:

.. code:: sh

   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"

Install the Python build dependencies for your platform,
using one of the commands listed in the
`official instructions`__.

__ https://github.com/pyenv/pyenv/wiki/Common-build-problems

Install the latest point release of every supported Python version.
This project template supports Python 3.6, 3.7, 3.8, and 3.9.

.. code:: console

   $ pyenv install 3.6.12
   $ pyenv install 3.7.9
   $ pyenv install 3.8.6
   $ pyenv install 3.9.0

After creating your project (see :ref:`below <Creating a project>`),
you can make these Python versions accessible in the project directory,
using the following command:

.. code:: console

   $ pyenv local 3.9.0 3.8.6 3.7.9 3.6.12

The first version listed is the one used when you type plain ``python``.
Every version can be used by invoking ``python<major.minor>``.
For example, use ``python3.7`` to invoke Python 3.7.


Requirements
------------

.. note::

   It is recommended to use pipx_ to install Python tools
   which are not specific to a single project.
   Please refer to the official documentation
   for detailed installation and usage instructions.
   If you decide to skip ``pipx`` installation,
   use `pip install`_ with the ``--user`` option instead.

.. _pip install: https://pip.pypa.io/en/stable/reference/pip_install/

You need four tools to use this template:

- Cookiecutter_ to create projects from the template,
- Nox_ to automate checks and other tasks

Install Cookiecutter_ using pipx:

.. code:: console

   $ pipx install cookiecutter

Project creation
~~~~~~~~~~~~~~~~

.. _Creating a project:

Creating a project
------------------

Create a project from this template
by pointing Cookiecutter to its `GitHub repository <Hypermodern Python Cookiecutter_>`__.
Use the ``--checkout`` option with the `current stable release <2021.7.15_>`__:

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
     --checkout="2021.7.15"

Cookiecutter downloads the template,
and asks you a series of questions about project variables,
for example, how you wish your project to be named.
When you have answered these questions,
your project is generated in the current directory,
using a subdirectory with the same name as your project.

Here is a complete list of the project variables defined by this template:

.. table:: Project variables
   :class: hypermodern-table
   :widths: auto

   ====================== ================================= ===================================
   Variable               Description                       Example
   ====================== ================================= ===================================
   ``project_name``       Project name on PyPI and GitHub   ``hypermodern-python``
   ``package_name``       Import name of the package        ``hypermodern_python``
   ``friendly_name``      Friendly project name             ``Hypermodern Python``
   ``author``             Primary author                    Katherine Johnson
   ``email``              E-mail address of the author      katherine@example.com
   ``github_user``        GitHub username of the author     ``katherine``
   ``version``            Initial project version           ``0.0.0``
   ``development_status`` Development status of the project ``Development Status :: 3 - Alpha``
   ====================== ================================= ===================================

.. note::

   The initial project version should be the latest release on PyPI_,
   or ``0.0.0`` for an unreleased package.
   See `The Release workflow`_ for details.

Your choices are recorded in the file ``.cookiecutter.json`` in the generated project,
together with the URL of this Cookiecutter template.
Having this JSON_ file in the project makes it possible later on
to update your project with changes from the Cookiecutter template,
using tools such as cupper_.

.. _JSON: https://www.json.org/
.. _cupper: https://github.com/senseyeio/cupper

In the remainder of this guide,
``<project>`` and ``<package>`` are used
to refer to the project and package names, respectively.
By default, their only difference is that
the project name uses hyphens (*kebab case*),
whereas the package name uses underscores (*snake case*).


Uploading to GitHub
-------------------

This project template is designed for use with GitHub_.
After generating the project,
your next steps are to create a Git repository and upload it to GitHub.

Change to the root directory of your new project,
initialize a Git repository, and
create a commit for the initial project structure.
In the commands below,
replace ``<project>`` by the name of your project.

.. code:: console

   $ cd <project>
   $ git init
   $ git add .
   $ git commit

Use the following command to ensure your default branch is called ``main``,
which is the `default branch name for GitHub repositories`__.

__ https://github.com/github/renaming

.. code:: console

   $ git branch --move --force main

Create an empty repository on GitHub_,
using the project name you chose when you generated the project.

.. note::

   Do not include a ``README.md``, ``LICENSE``, or ``.gitignore``.
   These files are provided by the project template.

Finally, upload your repository to GitHub.
In the commands below, replace ``<username>`` by your GitHub username,
and ``<project>`` by the name of your project.

.. code:: console

   $ git remote add origin git@github.com:<username>/<project>.git
   $ git push --set-upstream origin main

Now may be a good time to set up Continuous Integration for your repository.
Refer to the section :ref:`External services`
for detailed instructions.


Project overview
~~~~~~~~~~~~~~~~

Files and directories
---------------------

This section provides an overview of all the files generated for your project.

Let's start with the directory layout:

.. table:: Directories
   :class: hypermodern-table
   :widths: auto

   ===================================== ===============================
   ``<package>``                         Python package
   ``tests``                             Test suite
   ``docs``                              Documentation
   ``.github/workflows``                 GitHub Actions workflows
   ===================================== ===============================

The Python package is located in the ``<package>`` directory.
For more details on these files, refer to the section :ref:`The initial package`.

.. table:: Python package
   :class: hypermodern-table
   :widths: auto

   ===================================== ===============================
   ``<project>/__init__.py``             Package initialization
   ``<project>/main.py``                 Command-line interface
   ===================================== ===============================

The test suite is located in the ``tests`` directory.
For more details on these files, refer to the section :ref:`The test suite`.

.. table:: Test suite
   :class: hypermodern-table
   :widths: auto

   ===================================== ===============================
   ``tests/__init__.py``                 Test package initialization
   ``tests/test_main.py``                Test cases for ``main``
   ===================================== ===============================

The project documentation is written in reStructuredText_.
The documentation files in the top-level directory are rendered on GitHub_:

.. table:: Documentation files (top-level)
   :class: hypermodern-table
   :widths: auto

   ======================= ============================================
   ``README.rst``          Project description for GitHub and PyPI
   ======================= ============================================

The files in the ``docs`` directory are
built using :ref:`Sphinx <Documentation>` and
hosted on :ref:`Read the Docs <Read the Docs integration>`:

.. table:: Documentation files (Sphinx)
   :class: hypermodern-table
   :widths: auto

   ====================== =======================================================
   ``index.rst``          Main document
   ====================== =======================================================

The ``.github/workflows`` directory contains the :ref:`GitHub Actions workflows <GitHub Actions workflows>`:

.. table:: GitHub Actions workflows
   :class: hypermodern-table
   :widths: auto

   ======================= ===============================
   ``release.yml``         :ref:`The Release workflow`
   ``tests.yml``           :ref:`The Tests workflow`
   ``labeler.yml``         :ref:`The Labeler workflow`
   ======================= ===============================

The project contains many configuration files for developer tools.
Most of these are located in the top-level directory.
The table below lists these files,
and links each file to a section with more details.

.. table:: Configuration files
   :class: hypermodern-table
   :widths: auto

   ===================================== ========================================
   ``.cookiecutter.json``                :ref:`Project variables <Creating a project>`
   ``.darglint``                         Configuration for :ref:`darglint <darglint integration>`
   ``.github/dependabot.yml``            Configuration for :ref:`Dependabot <Dependabot integration>`
   ``.flake8``                           Configuration for :ref:`Flake8 <The Flake8 hook>`
   ``.gitattributes``                    `Git attributes <.gitattributes_>`__
   ``.gitignore``                        `Git ignore file <.gitignore_>`__
   ``.github/release-drafter.yml``       Configuration for :ref:`Release Drafter <The Release workflow>`
   ``.github/labels.yml``                Configuration for :ref:`GitHub Labeler <The Labeler workflow>`
   ``.pre-commit-config.yaml``           Configuration for :ref:`pre-commit <Linting with pre-commit>`
   ``.readthedocs.yml``                  Configuration for :ref:`Read the Docs <Read the Docs integration>`
   ``codecov.yml``                       Configuration for :ref:`Codecov <Codecov integration>`
   ``docs/conf.py``                      Configuration for :ref:`Sphinx <Documentation>`
   ``noxfile.py``                        Configuration for :ref:`Nox <Using Nox>`
   ``pyproject.toml``                    Configuration for many pre-commit hooks and other tools.
   ===================================== ========================================

.. _.gitignore: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring

The table below lists some additional files with pinned dependencies.
Follow the links for more details on these.

.. table:: Dependency files
   :class: hypermodern-table
   :widths: auto

   ===================================== ================================
   ``docs/requirements.txt``             Requirements file for :ref:`Read the Docs <Read the Docs integration>`
   ``.github/workflows/constraints.txt`` Constraints file for :ref:`GitHub Actions workflows <Workflow constraints>`
   ===================================== ================================


.. _The initial package:

The initial package
-------------------

You can find the initial Python package in your generated project
under the ``<package>`` directory::

   <package>
       ├── __init__.py
       └── main.py

``__init__.py``
   This file declares the directory as a `Python package`_,
   and contains any package initialization code.

   .. _Python package: https://docs.python.org/3/tutorial/modules.html#packages

.. _The test suite:

The test suite
--------------

Tests are written using the pytest_ testing framework,
the *de facto* standard for testing in Python.

The test suite is located in the ``tests`` directories within <package>::

   tests
   └── test_main.py

The file ``test_main.py`` contains tests for the ``main`` module.

Initially, the test suite contains a single test case,
checking whether the program exits with a status code of zero.
It also provides a `test fixture`_ using `click.testing.CliRunner`_,
a helper class for invoking the program from within tests.

.. _test fixture: https://docs.pytest.org/en/latest/explanation/fixtures.html#about-fixtures
.. _click.testing.CliRunner: https://click.palletsprojects.com/en/7.x/testing/

For details on how to run the test suite,
refer to the section :ref:`The tests session`.


.. _Documentation:

Documentation
-------------

The project documentation is written in reStructuredText_
and processed by the Sphinx_ documentation engine.

The top-level directory contains several stand-alone documentation files:

``README.rst``
   This file is your main project page and displayed on GitHub and PyPI.


.. _Contributor Covenant: https://www.contributor-covenant.org

.. note::

   The files above are also rendered on GitHub and PyPI.
   Keep them in plain reStructuredText, without Sphinx extensions.

The documentation files in the ``docs`` directory are built using Sphinx_:

``index.rst``
   This is the main documentation page.
   This file also defines the navigation menu,
   with links to other documentation pages.
   The *Changelog* menu entry
   links to the `GitHub Releases <GitHub Release_>`__ page of your project.

``reference.rst``
   The API reference for your project.
   It is generated from docstrings and type annotations in the source code,
   using the autodoc_ and napoleon_ extensions.

``usage.rst``
   The command-line reference for your project.
   It is generated by inspecting the click entry-point in your package,
   using the sphinx-click extension.

The ``docs`` directory contains two more files:

``conf.py``
   This Python file contains the `Sphinx configuration`__.

__ https://www.sphinx-doc.org/en/master/usage/configuration.html

``requirements.txt``
   The requirements file pins the build dependencies for the Sphinx documentation.
   This file is only used on Read the Docs.

The project documentation is built and hosted on
:ref:`Read the Docs <Read the Docs integration>`,
and uses their official theme sphinx-rtd-theme_.

You can also build the documentation locally using Nox,
see :ref:`The docs session`.


.. _Using Nox:

Using Nox
~~~~~~~~~

Nox_ automates testing in multiple Python environments.
Like its older sibling tox_,
Nox makes it easy to run any kind of job in an isolated environment,
with only those dependencies installed that the job needs.

.. _tox: https://tox.readthedocs.io/

Nox sessions are defined in a Python file
named ``noxfile.py`` and located in the project directory.
They consist of a virtual environment
and a set of commands to run in that environment.

While Poetry environments allow you to
interact with your package during development,
Nox environments are used to run developer tools
in a reliable and repeatable way across Python versions.

Most sessions are run with every supported Python version.
Other sessions are only run with the current stable Python version,
for example the session used to build the documentation.


Running sessions
----------------

If you invoke Nox by itself, it will run the full test suite:

.. code:: console

   $ nox

This includes tests, linters, type checks, and more.
For the full list, please refer to the table `below <Table of Nox sessions_>`_.

The list of sessions run by default can be configured
by editing ``nox.options.sessions`` in ``noxfile.py``.
Currently the list only excludes the `docs session <The docs session_>`_
(which spawns an HTTP server)
and the `coverage session <The coverage session_>`_
(which is triggered by the `tests session <The tests session_>`_).

You can also run a specific Nox session, using the ``--session`` option.
For example, build the documentation like this:

.. code:: console

   $ nox --session=docs

Print a list of the available Nox sessions
using the ``--list-sessions`` option:

.. code:: console

   $ nox --list-sessions

Nox creates virtual environments from scratch on each invocation.
You can speed things up by passing the
`--reuse-existing-virtualenvs`_ option,
or the equivalent short option ``-r``.
For example, the following may be more practical during development
(this will only run tests and type checks, on the current Python release):

.. code:: console

   $ nox -p 3.9 -rs tests mypy

.. _--reuse-existing-virtualenvs: https://nox.thea.codes/en/stable/usage.html#re-using-virtualenvs

Many sessions accept additional options after ``--`` separator.
For example, the following command runs a specific test module:

.. code:: console

   $ nox --session=tests -- tests/test_main.py


Overview of Nox sessions
------------------------

.. _Table of Nox sessions:

The following table gives an overview of the available Nox sessions:

.. table:: Nox sessions
   :class: hypermodern-table
   :widths: auto

   ========================================== ===================================== ================== =========
   Session                                    Description                           Python              Default
   ========================================== ===================================== ================== =========
   :ref:`coverage <The coverage session>`     Report coverage with Coverage.py_     ``3.9``               (✓)
   :ref:`docs <The docs session>`             Build and serve Sphinx_ documentation ``3.9``
   :ref:`docs-build <The docs-build session>` Build Sphinx_ documentation           ``3.9``                ✓
   :ref:`pre-commit <The pre-commit session>` Lint with pre-commit_                 ``3.9``                ✓
   :ref:`tests <The tests session>`           Run tests with pytest_                ``3.6`` … ``3.9``      ✓
   :ref:`xdoctest <The xdoctest session>`     Run examples with xdoctest_           ``3.6`` … ``3.9``      ✓
   ========================================== ===================================== ================== =========


.. _The docs session:

The docs session
----------------

Build the documentation using the Nox session ``docs``:

.. code:: console

   $ nox --session=docs

The docs session runs the command ``sphinx-autobuild`` to generate the HTML documentation from the Sphinx directory.
This tool has several advantages over ``sphinx-build`` when you are editing the documentation files:

- It rebuilds the documentation whenever a change is detected.
- It spins up a web server with live reloading.
- It opens the location of the web server in your browser.

Use the ``--`` separator to pass additional options.
For example, to treat warnings as errors and run in nit-picky mode:

.. code:: console

   $ nox --session=docs -- -W -n docs docs/_build

This Nox session always runs with the current major release of Python.


.. _The docs-build session:

The docs-build session
----------------------

The ``docs-build`` session runs the command ``sphinx-build`` to generate the HTML documentation from the Sphinx directory.

This session is meant to be run as a part of automated checks.
Use the interactive ``docs`` session instead while you're editing the documentation.

This Nox session always runs with the current major release of Python.


.. _The mypy session:

The mypy session
----------------

mypy_ is the pioneer and *de facto* reference implementation of static type checking in Python.

Run mypy using Nox:

.. code:: console

   $ nox --session=mypy

You can also run the type checker with a specific Python version.
For example, the following command runs mypy
using the current stable release of Python:

.. code:: console

   $ nox --session=mypy --python=3.9

Use the separator ``--`` to pass additional options and arguments to ``mypy``.
For example, the following command type-checks only the ``main`` module:

.. code:: console

   $ nox --session=mypy -- <package>/main.py


.. _The pre-commit session:

The pre-commit session
----------------------

pre-commit_ is a multi-language linter framework and a Git hook manager.
Learn more about it in the section :ref:`Linting with pre-commit`.

Run pre-commit from Nox using the ``pre-commit`` session:

.. code:: console

   $ nox --session=pre-commit

This session always runs with the current stable release of Python.

Use the separator ``--`` to pass additional options to ``pre-commit``.
For example, the following command installs the pre-commit hooks,
so they run automatically on every commit you make:

.. code:: console

   $ nox --session=pre-commit -- install

.. _The tests session:

The tests session
-----------------

Tests are written using the pytest_ testing framework.
Learn more about it in the section :ref:`The test suite`.

Run the test suite using the Nox session ``tests``:

.. code:: console

   $ nox --session=tests

The tests session runs the test suite against the installed code.
More specifically, the session builds a wheel from your project and
installs it into the Nox environment,
with dependencies pinned as specified by Poetry's lock file.

You can also run the test suite with a specific Python version.
For example, the following command runs the test suite
using the current stable release of Python:

.. code:: console

   $ nox --session=tests --python=3.9

Use the separator ``--`` to pass additional options to ``pytest``.
For example, the following command runs only the test case ``test_main_succeeds``:

.. code:: console

   $ nox --session=tests -- -k test_main_succeeds

The tests session also installs pygments_, a Python syntax highlighter.
It is used by pytest to highlight code in tracebacks,
improving the readability of test failures.


.. _The coverage session:

The coverage session
--------------------

.. note::

   *Test coverage* is a measure of the degree to which
   the source code of your program is executed
   while running its test suite.

The coverage session prints a detailed coverage report to the terminal,
combining the coverage data collected
during the :ref:`tests session <The tests session>`.
If the total coverage is below 100%,
the coverage session fails.
Code coverage is measured using `Coverage.py`_.

The coverage session is triggered by the tests session,
and runs after all other sessions have completed.
This allows it to combine the coverage data for different Python versions.

You can also run the session manually:

.. code:: console

   $ nox --session=coverage

Use the ``--`` separator to pass arguments to the ``coverage`` command.
For example, here's how you would generate an HTML report
in the ``htmlcov`` directory:

.. code:: console

   $ nox -rs coverage -- html

Coverage.py_ is configured in the ``pyproject.toml`` file,
using the ``tool.coverage`` table.
The configuration informs the tool about your package name and source tree layout.
It also enables branch analysis and the display of line numbers for missing coverage,
and specifies the target coverage percentage.

During continuous integration,
coverage data is uploaded to the Codecov_ reporting service.
For details, see the sections about
:ref:`Codecov <Codecov integration>` and
:ref:`The Tests workflow`.


.. _The xdoctest session:

The xdoctest session
--------------------

The xdoctest_ tool
runs examples in your docstrings and
compares the actual output to the expected output as per the docstring.
This serves multiple purposes:

- The example is checked for correctness.
- You ensure that the documentation is up-to-date.
- Your codebase gets additional test coverage for free.

Run the tool using the Nox session ``xdoctest``:

.. code:: console

   $ nox --session=xdoctest

You can also run the test suite with a specific Python version.
For example, the following command runs the examples
using the current stable release of Python:

.. code:: console

   $ nox --session=xdoctest --python=3.9

By default, the Nox session uses the ``all`` subcommand to run all examples.
You can also list examples using the ``list`` subcommand,
or run specific examples:

.. code:: console

   $ nox --session=xdoctest -- list


.. _Linting with pre-commit:

Linting with pre-commit
~~~~~~~~~~~~~~~~~~~~~~~

pre-commit_ is a multi-language linter framework and a Git hook manager.
It allows you to
integrate linters and formatters into your Git workflow,
even when written in a language other than Python.

pre-commit is configured using the file ``.pre-commit-config.yaml``
in the project directory.
Please refer to the `official documentation`__
for details about the configuration file.

__ https://pre-commit.com/#adding-pre-commit-plugins-to-your-project


Running pre-commit from Nox
---------------------------

pre-commit runs in a Nox session every time you invoke ``nox``:

.. code:: console

   $ nox

Run the pre-commit session explicitly like this:

.. code:: console

   $ nox --session=pre-commit

The session is described in more detail in the section :ref:`The pre-commit session`.


Running pre-commit from git
---------------------------

When installed as a `Git hook`_,
pre-commit runs automatically every time you invoke ``git commit``.
The commit is aborted if any check fails.
When invoked in this mode, pre-commit only runs on files staged for the commit.

.. _Git hook: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks

Install pre-commit as a Git hook by running the following command:

.. code:: console

   $ nox --session=pre-commit -- install


Managing hooks with pre-commit
------------------------------

Hooks in languages other than Python, such as ``prettier``,
run in isolated environments managed by pre-commit.
To upgrade these hooks, use the autoupdate__ command:

__ https://pre-commit.com/#pre-commit-autoupdate

.. code:: console

   $ nox --session=pre-commit -- autoupdate


Python-language hooks
---------------------

.. note::

   This section provides some background information about
   how this project template integrates pre-commit with Poetry and Nox.
   You can safely skip this section.

Python-language hooks in the |HPC| are not managed by pre-commit.
Instead, they are tracked as development dependencies in Poetry,
and installed into the Nox session alongside pre-commit itself.
As development dependencies, they are also present in the Poetry environment.

This approach has some advantages:

- All project dependencies are managed by Poetry.
- Hooks receive automatic upgrades from Dependabot.
- Nox can serve as a single entry point for all checks.
- Additional hook dependencies can be upgraded by a dependency manager.
  An example for this are Flake8 extensions.
  By contrast, ``pre-commit autoupdate`` does not include additional dependencies.
- Dependencies of dependencies (*subdependencies*) can be locked automatically,
  making checks more repeatable and deterministic.
- Linters and formatters are available in the Poetry environment,
  which is useful for editor integration.

There are also some drawbacks to this technique:

- This is not the officially supported way to integrate pre-commit hooks.
- The hook scripts installed by pre-commit do not activate the virtual environment
  in which pre-commit and the hooks are installed.
  To work around this limitation,
  the Nox session patches hook scripts on installation.
- Adding a hook is more work,
  including updating ``pyproject.toml`` and ``noxfile.py``, and
  adding the hook definition to ``pre-commit-config.yaml``.

You can always opt out of this integration method,
by removing the ``repo: local`` section from the configuration file,
and adding the official pre-commit hooks instead.
Don't forget to remove the hooks from Poetry's dependencies and from the Nox session.

.. note::

   Python-language hooks in the |HPC| are defined as `system hooks`__.
   System hooks don't have their environments managed by pre-commit;
   instead, pre-commit assumes that hook dependencies have already been installed
   and are available in its environment.
   The Nox session for pre-commit takes care of
   installing the Python hooks alongside pre-commit.

   __ https://pre-commit.com/#system

   Furthermore, the |HPC| defines Python-language hooks as `repository-local hooks`__.
   As such, hook definitions are not supplied by the hook repositories,
   but by the project itself.
   This makes it possible to override the hook language to ``system``, as explained above.

   __ https://pre-commit.com/#repository-local-hooks


Adding an official pre-commit hook
----------------------------------

Adding the official pre-commit hook for a linter is straightforward.
Often you can simply copy a configuration snippet from the repository's ``README``.
Otherwise, note the hook identifier from the ``pre-commit-hooks.yaml`` file,
and the git tag for the latest version.
Add the following section to your ``pre-commit-config.yaml``, under ``repos``:

.. code:: yaml

   - repo: <hook repository>
     rev: <version tag>
     hooks:
       - id: <hook identifier>

While this technique also works for Python-language hooks,
it is recommended to integrate Python hooks with Nox and Poetry,
as shown in the next section.


Adding a Python-language hook
-----------------------------

Adding a Python-language hook to your project takes three steps:

- Add the hook as a Poetry development dependency.
- Install the hook in the Nox session for pre-commit.
- Add the hook to ``pre-commit-config.yaml``.

For example, consider a linter named ``awesome-linter``.

First, use Poetry to add the linter to your development dependencies:

.. code:: console

   $ poetry add --dev awesome-linter

Next, update ``noxfile.py`` to add the linter to the pre-commit session:

.. code:: python

   @nox.session(name="pre-commit", ...)
   def precommit(session: Session) -> None:
       ...
       session.install(
           "awesome-linter",  # Install awesome-linter
           "black",
           "darglint",
           ...
       )

Finally, add the hook to ``pre-commit-config.yaml`` as follows:

- Locate the ``pre-commit-hooks.yaml`` file in the ``awesome-linter`` repository.
- Copy the entry for the hook (not just the hook identifier).
- Change ``language:`` from ``python`` to ``system``.
- Add the hook definition to the ``repo: local`` section.

Depending on the linter, the hook definition might look somewhat like the following:

.. code:: yaml

   repos:
     - repo: local
       hooks:
         # ...
         - id: awesome-linter
           name: Awesome Linter
           entry: awesome-linter
           language: system  # was: python
           types: [python]


Running checks on modified files
--------------------------------

pre-commit runs checks on the *staged* contents of files.
Any local modifications are stashed for the duration of the checks.
This is motivated by pre-commit's primary use case,
validating changes staged for a commit.

Requiring changes to be staged allows for a nice property:
Many pre-commit hooks support fixing offending lines automatically,
for example ``black``, ``prettier``, and ``reorder-python-imports``.
When this happens,
your original changes are in the staging area,
while the fixes are in the work tree.
You can accept the fixes by staging them with ``git add``
before committing again.

If you want to run linters or formatters on modified files,
and you do not want to stage the modifications just yet,
you can also invoke the tools via Poetry instead.
For example, use ``poetry run flake8 <file>`` to lint a modified file with Flake8.


Overview of pre-commit hooks
----------------------------

The |HPC| comes with a pre-commit configuration consisting of the following hooks:

.. table:: pre-commit hooks
   :class: hypermodern-table
   :widths: auto

   ======================== ===============================================
   `black <Black_>`__       Run the Black_ code formatter
   `flake8 <Flake8_>`__     Run the Flake8_ linter
   `prettier <Prettier_>`__ Run the Prettier_ code formatter
   check-added-large-files_ Prevent giant files from being committed
   check-toml_              Validate TOML_ files
   check-yaml_              Validate YAML_ files
   end-of-file-fixer_       Ensure files are terminated by a single newline
   reorder-python-imports_  Rewrites source to reorder python imports
   trailing-whitespace_     Ensure lines do not contain trailing whitespace
   ======================== ===============================================

.. _check-toml: https://github.com/pre-commit/pre-commit-hooks#check-toml
.. _check-yaml: https://github.com/pre-commit/pre-commit-hooks#check-yaml
.. _check-added-large-files: https://github.com/pre-commit/pre-commit-hooks#check-added-large-files
.. _end-of-file-fixer: https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer
.. _trailing-whitespace: https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace


The Black hook
--------------

Black_ is the uncompromising Python code formatter.
One of its greatest features is its lack of configurability.
Blackened code looks the same regardless of the project you're reading.


The Prettier hook
-----------------

Prettier_ is an opinionated code formatter for many languages,
including YAML, Markdown, and JavaScript.
Like Black, it has few options,
and the |HPC| uses none of them.


.. _The Flake8 hook:

The Flake8 hook
---------------

Flake8_ is an extensible linter framework for Python.
For more details, see the section :ref:`Linting with Flake8`.


The reorder-python-imports hook
-------------------------------

reorder-python-imports_ sorts imports in your Python code.
Imports are separated into three sections,
as recommended by `PEP 8`_: standard library, third party, first party.
The tool also splits ``from`` imports onto separate lines to avoid merge conflicts,
and moves them after normal imports.
Any duplicate imports are removed.


Hooks from pre-commit-hooks
---------------------------

The pre-commit configuration also includes several smaller hooks
from the pre-commit-hooks_ repository.


.. _Linting with Flake8:

Linting with Flake8
~~~~~~~~~~~~~~~~~~~

Flake8_ is an extensible linter framework for Python,
and a command-line utility to run the linters on your source code.
The |HPC| integrates Flake8 via a pre-commit_ hook,
see the section :ref:`The Flake8 hook`.

The configuration file for Flake8 and its extensions
is named ``.flake8`` and located in the project directory.
For details about the configuration file, see the `official reference`__.

__ https://flake8.pycqa.org/en/latest/user/configuration.html

The sections below describe the linters in more detail.
Each section also notes any configuration settings applied by the |HPC|.

.. _Flake8: http://flake8.pycqa.org

.. _darglint integration:

darglint
--------

darglint_ checks that docstring descriptions match function definitions.
The tool has its own configuration file, named ``.darglint``.

`Error codes`__ are prefixed by ``DAR`` for "darglint".

.. _darglint codes:
__ https://github.com/terrencepreilly/darglint#error-codes

The |HPC| allows one-line docstrings without function signatures.
Multi-line docstrings must
specify the function signatures completely and correctly,
using `Google docstring style`_.

.. _Google docstring style: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings


.. _External services:

External services
~~~~~~~~~~~~~~~~~

Your GitHub repository can be integrated with several external services
for continuous integration and delivery.
This section describes these external services,
what they do, and how to set them up for your repository.


PyPI
----

PyPI_ is the official Python Package Index.
Uploading your package to PyPI allows others to
download and install it to their system.

Follow these steps to set up PyPI for your repository:

1. Sign up at PyPI_.
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named ``PYPI_TOKEN`` with the token you just copied.

PyPI is integrated with your repository
via the :ref:`Release workflow <The Release workflow>`.


TestPyPI
--------

TestPyPI_ is a test instance of the Python package registry.
It allows you to check your release before uploading it to the real index.

Follow these steps to set up TestPyPI for your repository:

1. Sign up at TestPyPI_.
2. Go to the Account Settings on TestPyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named ``TEST_PYPI_TOKEN`` with the token you just copied.

TestPyPI is integrated with your repository
via the :ref:`Release workflow <The Release workflow>`.


.. _Codecov integration:

Codecov
-------

Codecov_ is a reporting service for code coverage.

Follow these steps to set up Codecov for your repository:

1. Sign up at Codecov_.
2. Install their GitHub app.

The configuration is included in the repository,
in the file `codecov.yml`__.

__ https://docs.codecov.io/docs/codecov-yaml

Codecov integrates with your repository
via its GitHub app.
The :ref:`Tests workflow <The Tests workflow>` uploads the coverage data.


.. _Dependabot integration:

Dependabot
----------

Dependabot_ creates pull requests with automated dependency updates.


Please refer to the `official documentation`__ for more details.

__ https://docs.github.com/en/github/administering-a-repository/keeping-your-dependencies-updated-automatically

The configuration is included in the repository,
in the file `.github/dependabot.yml`__.

__ https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates


It manages the following dependencies:

.. table::
   :class: hypermodern-table
   :widths: auto

   =================== ===================================== ================================================
   Type of dependency  Managed files                         See also
   =================== ===================================== ================================================
   Python              ``docs/requirements.txt``             :ref:`Read the Docs <Read the Docs integration>`
   Python              ``.github/workflows/constraints.txt`` :ref:`Workflow constraints`
   GitHub Action       ``.github/workflows/*.yml``           :ref:`GitHub Actions workflows`
   =================== ===================================== ================================================


.. _Read the Docs integration:

Read the Docs
-------------

`Read the Docs`_ automates the building, versioning, and hosting of documentation.

Follow these steps to set up Read the Docs for your repository:

1. Sign up at `Read the Docs`_.
2. Import your GitHub repository,
   using the button *Import a Project*.
3. Install the GitHub webhook__,
   using the button *Add integration*
   on the *Integrations* tab
   in the *Admin* section of your project
   on Read the Docs.

__ https://docs.readthedocs.io/en/stable/webhooks.html

Read the Docs automatically starts building your documentation,
and will continue to do so when you push to the default branch or make a release.
Your documentation now has a public URL like this:

   *https://<project>.readthedocs.io/*

The configuration for Read the Docs is included in the repository,
in the file `.readthedocs.yml`__.
The |HPC| configures Read the Docs
to build and install the package with Poetry,
using a so-called `PEP 517`_-build.

__ https://docs.readthedocs.io/en/stable/config-file/v2.html

Build dependencies for the documentation
are installed using a requirements file located at ``docs/requirements.txt``.
Read the Docs currently does not support
installing development dependencies using Poetry's lock file.
For the sake of brevity and maintainability,
only direct dependencies are included.

.. note::

   The requirements file is managed by :ref:`Dependabot <Dependabot integration>`.
   When newer versions of the build dependencies become available,
   Dependabot updates the requirements file and submits a pull request.
   When adding or removing Sphinx extensions using Poetry,
   don't forget to update the requirements file as well.


.. _GitHub Actions workflows:

GitHub Actions workflows
~~~~~~~~~~~~~~~~~~~~~~~~

The |HPC| uses `GitHub Actions`_
to implement continuous integration and delivery.
With GitHub Actions,
you define so-called workflows
using YAML_ files located in the ``.github/workflows`` directory.

A *workflow* is an automated process
consisting of one or many jobs,
each of which executes a series of steps.
Workflows are triggered by events,
for example when a commit is pushed
or when a release is published.
You can learn more about
the workflow language and its supported keywords
in the `official reference`__.

__ https://help.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions

.. note::

   Real-time logs for workflow runs are available
   from the *Actions* tab in your GitHub repository.


Overview of workflows
---------------------

The |HPC| defines the following workflows:

.. table:: GitHub Actions workflows
   :class: hypermodern-table
   :widths: auto

   ===================================================== ======================== ==================================== =====================
   Workflow                                              File                     Description                          Trigger
   ===================================================== ======================== ==================================== =====================
   :ref:`Tests <The Tests workflow>`                     ``tests.yml``            Run the test suite with Nox_         Push, PR
   :ref:`Release <The Release workflow>`                 ``release.yml``          Upload the package to PyPI_          Push (default branch)
   :ref:`Labeler <The Labeler workflow>`                 ``labeler.yml``          Manage GitHub project labels         Push (default branch)
   ===================================================== ======================== ==================================== =====================


Overview of GitHub Actions
--------------------------

Workflows use the following GitHub Actions:

.. table:: GitHub Actions
   :class: hypermodern-table
   :widths: auto

   ============================================ =========================================================
   `actions/cache`_                             Cache dependencies and build outputs
   `actions/checkout`_                          Check out the Git repository
   `actions/download-artifact`_                 Download artifacts from workflows
   `actions/setup-python`_                      Set up workflows with a specific Python version
   `actions/upload-artifact`_                   Upload artifacts from workflows
   `codecov/codecov-action`_                    Upload coverage to Codecov
   `crazy-max/ghaction-github-labeler`_         Manage labels on GitHub as code
   `pypa/gh-action-pypi-publish`_               Upload packages to PyPI and TestPyPI
   `release-drafter/release-drafter`_           Draft and publish GitHub Releases
   `salsify/action-detect-and-tag-new-version`_ Detect and tag new versions in a repository
   ============================================ =========================================================

.. _actions/cache: https://github.com/actions/cache
.. _actions/checkout: https://github.com/actions/checkout
.. _actions/download-artifact: https://github.com/actions/download-artifact
.. _actions/setup-python: https://github.com/actions/setup-python
.. _actions/upload-artifact: https://github.com/actions/upload-artifact
.. _codecov/codecov-action: https://github.com/codecov/codecov-action
.. _crazy-max/ghaction-github-labeler: https://github.com/crazy-max/ghaction-github-labeler
.. _pypa/gh-action-pypi-publish: https://github.com/pypa/gh-action-pypi-publish
.. _release-drafter/release-drafter: https://github.com/release-drafter/release-drafter
.. _salsify/action-detect-and-tag-new-version: https://github.com/salsify/action-detect-and-tag-new-version

.. note::

   GitHub Actions used by the workflows are managed by :ref:`Dependabot <Dependabot integration>`.
   When newer versions of GitHub Actions become available,
   Dependabot updates the workflows that use them and submits a pull request.


.. _Workflow constraints:

Constraints file
----------------

GitHub Actions workflows install the following tools:

- pip_
- virtualenv_
- Nox_

.. _virtualenv: https://virtualenv.pypa.io/

These dependencies are pinned using a `constraints file`_
located in ``.github/workflow/constraints.txt``.

.. _constraints file: https://pip.pypa.io/en/stable/user_guide/#constraints-files

.. note::

   The constraints file is managed by :ref:`Dependabot <Dependabot integration>`.
   When newer versions of the tools become available,
   Dependabot updates the constraints file and submits a pull request.


.. _The Tests workflow:

The Tests workflow
------------------

The Tests workflow runs checks using Nox.
It is triggered on every push to the repository,
and when a pull request is opened or receives new commits.

Each Nox session runs in a separate job,
using the current release of Python
and the `latest Ubuntu runner`__.
Selected Nox sessions also run on Windows and macOS,
and with older Python versions,
as shown in the table below:

__ https://help.github.com/en/actions/automating-your-workflow-with-github-actions/virtual-environments-for-github-hosted-runners#supported-runners-and-hardware-resources

.. table:: Jobs in the Tests workflow
   :class: hypermodern-table
   :widths: auto

   ========================================== ====================== ==================
   Nox session                                Platform               Python versions
   ========================================== ====================== ==================
   :ref:`pre-commit <The pre-commit session>` Ubuntu                 3.9
   :ref:`tests <The tests session>`           Ubuntu                 3.9, 3.8, 3.7, 3.6
   :ref:`tests <The tests session>`           Windows                3.9
   :ref:`tests <The tests session>`           macOS                  3.9
   :ref:`coverage <The coverage session>`     Ubuntu                 3.9
   :ref:`docs-build <The docs-build session>` Ubuntu                 3.8
   ========================================== ====================== ==================

The workflow uploads the generated documentation as a `workflow artifact`__.
Building the documentation only serves the purpose of catching issues in pull requests.
Builds on `Read the Docs`_ happen independently.

__ https://help.github.com/en/actions/configuring-and-managing-workflows/persisting-workflow-data-using-artifacts

The workflow also uploads coverage data to Codecov_ after running tests.
It generates a coverage report in Cobertura__ XML format,
using the :ref:`coverage session <The coverage session>`.
The report is uploaded
using the official `Codecov GitHub Action <codecov/codecov-action_>`__.

__ https://cobertura.github.io/cobertura/

The Tests workflow uses the following GitHub Actions:

- `actions/checkout`_ for checking out the Git repository
- `actions/setup-python`_ for setting up the Python interpreter
- `actions/download-artifact`_ to download the coverage data of each tests session
- `actions/cache`_ for caching pre-commit environments
- `actions/upload-artifact`_ to upload the generated documentation and the coverage data of each tests session
- `codecov/codecov-action`_ for uploading to Codecov_

The Tests workflow is defined in ``.github/workflows/tests.yml``.


.. _The Release workflow:

The Release workflow
--------------------

The Release workflow publishes your package on PyPI_, the Python Package Index.
The workflow also creates a version tag in the GitHub repository,
and publishes a GitHub Release using `Release Drafter`_.
The workflow is triggered on every push to the default branch.

Release steps only run if the package version was bumped.
If the package version did not change,
the package is instead uploaded to TestPyPI_ as a prerelease,
and only a draft GitHub Release is created.
TestPyPI is a test instance of the Python Package Index.

The Release workflow uses API tokens to access PyPI_ and TestPyPI_.
You can generate these tokens from your account settings on these services.
The tokens need to be stored as secrets in the repository settings on GitHub:

.. table:: Secrets
   :class: hypermodern-table
   :widths: auto

   =================== ===================
   ``PYPI_TOKEN``      PyPI_ API token
   ``TEST_PYPI_TOKEN`` TestPyPI_ API token
   =================== ===================

The Release workflow uses the following GitHub Actions:

- `actions/checkout`_ for checking out the Git repository
- `actions/setup-python`_ for setting up the Python interpreter
- `salsify/action-detect-and-tag-new-version`_ for tagging on version bumps
- `pypa/gh-action-pypi-publish`_ for uploading the package to PyPI or TestPyPI
- `release-drafter/release-drafter`_ for publishing the GitHub Release

Release notes are populated with the titles and authors of merged pull requests.
You can group the pull requests into separate sections
by applying labels to them, like this:

.. include:: quickstart.rst
   :start-after: table-release-drafter-sections-begin
   :end-before: table-release-drafter-sections-end

The workflow is defined in ``.github/workflows/release.yml``.
The Release Drafter configuration is located in ``.github/release-drafter.yml``.


.. _The Labeler workflow:

The Labeler workflow
--------------------

The Labeler workflow manages the labels used in GitHub issues
and pull requests based on a description file ``.github/labels.yaml``.
In this file each label is described with
a ``name``,
a ``description``
and a ``color``.
The workflow is triggered on every push to the default branch.

The workflow creates or updates project labels if they are missing
or different compared to the ``labels.yml`` file content.

The workflow does not delete labels already configured in the GitHub UI
and not in the ``labels.yml`` file.
You can change this behavior and add ignore patterns
in the settings of the workflow (see `GitHub Labeler`_ documentation).

The Labeler workflow uses the following GitHub Actions:

- `actions/checkout`_ for checking out the Git repository
- `crazy-max/ghaction-github-labeler`_ for updating the GitHub project labels

The workflow is defined in ``.github/workflows/labeler.yml``.
The GitHub Labeler configuration is located in ``.github/labels.yml``.


.. _Tutorials:

Tutorials
~~~~~~~~~

First, make sure you have all the :ref:`requirements <Installation>` installed.


.. _How to test your project:

How to test your project
------------------------

Run the test suite using :ref:`Nox <Using Nox>`:

.. code:: console

   $ nox -r


How to run your code
--------------------

First, install the project and its dependencies to the Poetry environment:

.. code:: console

   $ poetry install

Run an interactive session in the environment:

.. code:: console

   $ poetry run python

Invoke the command-line interface of your package:

.. code:: console

   $ poetry run <project>


How to push code changes
------------------------

Create a branch for your changes:

.. code:: console

   $ git switch --create my-topic-branch main

Create a series of small, single-purpose commits:

.. code:: console

   $ git add <files>
   $ git commit

Push your branch to GitHub:

.. code:: console

   $ git push --set-upstream origin my-topic-branch

The push triggers the following automated steps:

- :ref:`The test suite runs against your branch <The Tests workflow>`.


How to open a pull request
--------------------------

Open a pull request for your branch on GitHub:

1. Select your branch from the *Branch* menu.
2. Click **New pull request**.
3. Enter the title for the pull request.
4. Enter a description for the pull request.
5. Apply a :ref:`label identifying the type of change <The Release workflow>`
6. Click **Create pull request**.

Release notes are pre-filled with the titles of merged pull requests.


How to accept a pull request
----------------------------

If all checks are marked as passed,
merge the pull request using the squash-merge strategy (recommended):

1. Click **Squash and Merge**.
   (Select this option from the dropdown menu of the merge button, if it is not shown.)
2. Click **Confirm squash and merge**.
3. Click **Delete branch**.

This triggers the following automated steps:

- :ref:`The test suite runs against the main branch <The Tests workflow>`.
- :ref:`The draft GitHub Release is updated <The Release workflow>`.
- :ref:`A pre-release of the package is uploaded to TestPyPI <The Release workflow>`.
- `Read the Docs`_ rebuilds the *latest* version of the documentation.

In your local repository,
update the main branch:

.. code:: console

   $ git switch main
   $ git pull origin main

Optionally, remove the merged topic branch
from the local repository as well:

.. code:: console

   $ git remote prune origin
   $ git branch --delete --force my-topic-branch

The original commits remain accessible from the pull request
(*Commits* tab).


How to make a release
---------------------

Releases are triggered by a version bump on the default branch.
It is recommended to do this in a separate pull request:

1. Switch to a branch.
2. Bump the version using `poetry version`_.
3. Commit and push to GitHub.
4. Open a pull request.
5. Merge the pull request.

.. _poetry version: https://python-poetry.org/docs/cli/#version

The individual steps for bumping the version are:

.. code:: console

   $ git switch --create release main
   $ poetry version <version>
   $ git commit --message="<project> <version>" pyproject.toml
   $ git push origin release

If you're not sure which version number to choose,
read about `Semantic Versioning`_.
Versioning rules for Python packages are laid down in `PEP 440`_.

Before merging the pull request for the release,
go through the following checklist:

- The pull request passes all checks.
- The development release on TestPyPI_ looks good.
- All pull requests for the release have been merged.

Merging the pull request triggers the
:ref:`Release workflow <The Release workflow>`.
This workflow performs the following automated steps:

- Publish the package on PyPI.
- Publish a GitHub Release.
- Apply a Git tag to the repository.

`Read the Docs`_ automatically builds a new stable version of the documentation.


The Hypermodern Python blog
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The project setup is described in detail in the `Hypermodern Python`_ article series:

- `Chapter 1: Setup`__
- `Chapter 2: Testing`__
- `Chapter 3: Linting`__
- `Chapter 4: Typing`__
- `Chapter 5: Documentation`__
- `Chapter 6: CI/CD`__

__ https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
__ https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260
__ https://medium.com/@cjolowicz/hypermodern-python-3-linting-e2f15708da80
__ https://medium.com/@cjolowicz/hypermodern-python-4-typing-31bcf12314ff
__ https://medium.com/@cjolowicz/hypermodern-python-5-documentation-13219991028c
__ https://medium.com/@cjolowicz/hypermodern-python-6-ci-cd-b233accfa2f6

You can also read the articles on `this blog`__.

__ https://cjolowicz.github.io/posts/hypermodern-python-01-setup/

.. |HPC| replace:: *Hypermodern Python Cookiecutter*

.. include:: ../README.rst
   :start-after: references-begin
   :end-before: references-end

.. include:: ./quickstart.rst
   :start-after: quickstart-references-begin
   :end-before: quickstart-references-end

.. _Calendar Versioning: https://calver.org
.. _GitHub Release: https://help.github.com/en/github/administering-a-repository/about-releases
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _Jinja: https://palletsprojects.com/p/jinja/
.. _MIT license: https://opensource.org/licenses/MIT
.. _PEP 257: http://www.python.org/dev/peps/pep-0257/
.. _PEP 440: https://www.python.org/dev/peps/pep-0440/
.. _PEP 517: https://www.python.org/dev/peps/pep-0517/
.. _PEP 518: https://www.python.org/dev/peps/pep-0518/
.. _PEP 561: https://www.python.org/dev/peps/pep-0561/
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _TOML: https://github.com/toml-lang/toml
.. _YAML: https://yaml.org/
.. _bash: https://www.gnu.org/software/bash/
.. _curl: https://curl.haxx.se
.. _darglint: https://github.com/terrencepreilly/darglint
.. _flake8-bandit: https://github.com/tylerwince/flake8-bandit
.. _flake8-bugbear: https://github.com/PyCQA/flake8-bugbear
.. _flake8-docstrings: https://gitlab.com/pycqa/flake8-docstrings
.. _flake8-rst-docstrings: https://github.com/peterjc/flake8-rst-docstrings
.. _git: https://www.git-scm.com
.. _mccabe: https://github.com/PyCQA/mccabe
.. _pep8-naming: https://github.com/pycqa/pep8-naming
.. _pip: https://pip.pypa.io/
.. _pre-commit-hooks: https://github.com/pre-commit/pre-commit-hooks
.. _pycodestyle: https://pycodestyle.pycqa.org/en/latest/
.. _pydocstyle: http://www.pydocstyle.org/
.. _pyflakes: https://github.com/PyCQA/pyflakes
.. _pygments: https://pygments.org/
.. _reorder-python-imports: https://github.com/asottile/reorder_python_imports
.. _reStructuredText: https://docutils.sourceforge.io/rst.html
.. _sphinx-autobuild: https://github.com/executablebooks/sphinx-autobuild
.. _sphinx-rtd-theme: https://sphinx-rtd-theme.readthedocs.io
.. _Versions and constraints: https://python-poetry.org/docs/dependency-specification/
.. _Semantic Versioning: https://semver.org/
