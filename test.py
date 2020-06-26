import unittest
from unit_test import main
from unit_test import calculator


class TestMain(unittest.TestCase):

    def setUp(self):
        print(' test a function')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_add(self):
        test_num1 = 5
        test_num2 = 3
        result = calculator.add(test_num1, test_num2)
        self.assertEqual(result, 8)

    def test_sub(self):
        test_num1 = 5
        test_num2 = 3
        result = calculator.sub(test_num1, test_num2)
        self.assertEqual(result, 2)

    def test_mul(self):
        test_num1 = 5
        test_num2 = 3
        result = calculator.mul(test_num1, test_num2)
        self.assertEqual(result, 15)

    def test_div(self):
        test_num1 = 6
        test_num2 = 3
        result = calculator.div(test_num1, test_num2)
        self.assertEqual(result, 2)

    def test_rem(self):
        test_num1 = 5
        test_num2 = 3
        result = calculator.rem(test_num1, test_num2)
        self.assertEqual(result, 2)

    def tearDown(self):
        print('cleaning up ')


if __name__ == '__main__':
    unittest.main()
