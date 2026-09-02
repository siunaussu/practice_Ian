def my_decorator(data):
    def wrapper(func):
        def inner(*args, **kwargs):
            for a, b, c in data:
                func(a, b, c)
                print(f"\na: {a}, b: {b}, -> result: {c}")
        return inner
    return wrapper


list1 = [(1, 2, 3), (3, 4, 7)]

@my_decorator(list1)
def test_be_decorator(a, b, c):
    res = add_decorator(a, b)
    assert res == c


def add_decorator(a, b):
    return a + b


