import pytest


def add(a, b):
    return a + b


list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 1, 2]
list3 = [3]


@pytest.mark.parametrize('a', list1)
@pytest.mark.parametrize('b', list2)
@pytest.mark.parametrize('c', list2)
def test_add(a, b, c):
    result = add(a, b)
    assert result == c