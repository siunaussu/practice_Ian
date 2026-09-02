import unittest
from .practice_calculator import Calculator

class TestCalculator(unittest.TestCase):
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
    unittest.main()
