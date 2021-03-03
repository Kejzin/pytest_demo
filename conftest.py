import pytest


numbers1 = [1, 4, 5]
numbers2 = [1, 8, 5]


@pytest.fixture()
def welcome_to_tests():
    print("Hello tests")

