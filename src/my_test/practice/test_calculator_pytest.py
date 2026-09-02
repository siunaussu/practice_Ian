from .practice_calculator import Calculator


calculator = Calculator()

def test_add():
    assert calculator.add_number(1,2) == 3


def test_minus():
    assert calculator.minus_number(3, 2) == 1


def test_multi():
    assert calculator.multi_number(2, 4) == 8


def test_divide():
    assert calculator.divi_number(3, 2) == 1.5

