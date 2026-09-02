import unittest
from unittest.mock import Mock

from . import practice_mock


class TestMock(unittest.TestCase):

    def test_pay_success(self):
        practice_mock.pay_interface = Mock(return_value={'code': 200, 'msg': '支付成功'})
        result = practice_mock.pay()
        self.assertEqual(result, '支付成功', "判断是否支付成功。")


if __name__ == '__main__':
    suit = unittest.TestSuite()
    loader = unittest.TestLoader()

    suit.addTests(loader.loadTestsFromTestCase(TestMock))

    runner = unittest.TextTestRunner()

    runner.run(suit)

