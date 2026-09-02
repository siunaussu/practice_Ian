import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_case_1(self):
        print("test_case_1")

    def test_case_2(self):
        print("test_case_2")

    def test_case_3(self):
        print("test_case_3")

if __name__ == '__main__':
    unittest.main()
