import unittest

import sys

from .practice_calculator import Calculator

class TestCalculatorSuit(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()
        print(f"setUp {self._testMethodName} 开始测试")

    def tearDown(self) -> None:
        del self.calc
        print(f"tearDown {self._testMethodName} 测试结束")

    def test_add(self):
        """加"""
        self.assertEqual(self.calc.add_number(1, 3), 3, f"1 + 3 should equal 4")

    def test_minus(self):
        """减"""
        self.assertEqual(self.calc.minus_number(3, 2), 1, f"3 - 2 should equal 1")

    def test_multi(self):
        """乘"""
        self.assertEqual(self.calc.multi_number(2, 5), 10, f"2 * 5 should equal 10")

    def test_divi(self):
        """除"""
        self.assertEqual(self.calc.divi_number(10, 2), 5, f"10 / 2 should equal 5")


if __name__ == '__main__':
    suit = unittest.TestSuite()

    # 创建测试加载器
    loader = unittest.TestLoader()

    # 单条添加
    # suit.addTest(TestCalculatorSuit('test_add'))
    # suit.addTest(TestCalculatorSuit('test_divi'))

    # 批量添加
    # suit.addTests([TestCalculatorSuit('test_minus'), TestCalculatorSuit('test_multi')])
    # 通过加载器批量添加
    suit.addTests(loader.loadTestsFromTestCase(TestCalculatorSuit))  # 通过类，批量添加用例
    suit.addTests(loader.loadTestsFromModule(sys.modules[__name__])) # 通过模块名，批量添加用例
    suit.addTests(loader.discover('.', 'test_*.py'))    # 通过目录，指定起始目录，批量添加符合规则的用例

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)


