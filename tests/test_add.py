import pytest

from tested_functions import add


@pytest.mark.smoke
def test_add():
    result = add(1, 2)
    print("Here is test add")
    assert result == 3


def test_add_failing():
    """This test is designed to fail"""
    assert False
