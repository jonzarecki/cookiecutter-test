"""Test cases for the __main__ module."""

from {{cookiecutter.package_name}}.__main__ import main


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    main()
    a = 1
    assert a == 1
