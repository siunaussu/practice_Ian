import pytest


@pytest.fixture
def func_1():
    print("\nydc")
    return "YDC"

def test_2(func_1):
    print(func_1)

