import pytest
import csv

def get_data(file_name) -> list[list[int]]:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        next(data)
        data_list = [[int(i) for i in row] for row in data]

        return data_list


def func_add(a: int, b: int) -> int:
    return a + b


def test_add(data_factory):
    a, b, c = data_factory
    result = func_add(a, b)
    assert result == c


@pytest.fixture(params=get_data('data/number.csv'))
def data_factory(request):
    a, b, c = request.param
    print(f"\n setup: {a}, {b}, {c}")
    yield  a, b, c
    print(f"\n teardown: {a}, {b}, {c}")
