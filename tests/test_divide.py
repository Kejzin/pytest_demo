# Here is example of importing a whole file
import pytest

from conftest import numbers1
from conftest import numbers2

import tested_functions


def test_divide():
    result = tested_functions.divide(10, 5)  # Here is an example of using a function from inside of the imported file
    print("Here is test divide")
    assert result == 2.0


def test_divide_floats():
    print("Here I'm in test divide floats")
    result = tested_functions.divide(10.0, 1.1)
    assert isinstance(result, float)


def test_divide_small_floats():
    print("Here I'm in test divide small floats")
    result = tested_functions.divide(0.001, 0.002)
    assert result > float("-inf")


@pytest.mark.parametrize("number1", numbers1)
@pytest.mark.parametrize("number2", numbers2)
def test_divide_conftest_number(welcome_to_tests, number1, number2):
    result = tested_functions.divide(number1, number2)
    assert isinstance(result, float)
