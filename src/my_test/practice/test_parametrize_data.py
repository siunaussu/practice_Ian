import csv

import pytest


def get_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        data_list = [i for i in data]

        return data_list[1:]

@pytest.mark.parametrize("username,password", get_data('data/user.csv'))
def test_login(username, password):
    print(f"\n用户{username}，密码是{password}")