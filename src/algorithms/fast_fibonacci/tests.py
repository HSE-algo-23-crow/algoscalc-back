import unittest

from src.algorithms.fast_fibonacci.function import *


class TestCase(unittest.TestCase):
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]

    def test_fibonacci(self):
        for index, number in enumerate(self.numbers):
            self.assertEqual(main(str(index + 1)), {'result': str(number)})

    def test_raiseException1(self):
        self.assertRaises(ValueError, main, "-10")

    def test_raiseException2(self):
        self.assertRaises(ValueError, main, "0.1")

    def test_raiseException3(self):
        self.assertRaises(ValueError, main, "a")


if __name__ == '__main__':
    unittest.main()
