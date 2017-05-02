import unittest

from testing.testing.Calc import Calc


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(1, 3))

    def test_add_method_raises_type_error_if_non_ints_are_passed(self):
        self.assertRaises(TypeError, self.calc.add, "s", 1)


if __name__ == '__main__':
    unittest.main()
