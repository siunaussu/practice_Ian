import pytest

user_date = [
    (1, 'ydc1', 20),
    (2, 'ydc2', 21),
    (3, 'ydc3', 23),
]

@pytest.fixture(params=user_date)
def user_fixture(request):
    return  request.param

def test_login(user_fixture):
    no, name, age = user_fixture
    print(f'\n{no}号，登录用户{name},{age}岁')

