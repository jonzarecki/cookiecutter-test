# pylint: disable=redefined-outer-name
import pytest

from {{cookiecutter.package_name}}.utils.example_util import _util_function


@pytest.fixture
def setup1() -> int:
    return _util_function()


def test_something(setup1: int) -> None:
    print(setup1)
    assert setup1 == 3, "always right"
