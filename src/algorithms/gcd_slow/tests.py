import unittest

from src.algorithms.gcd_slow.function import gcd


A = 0
"""Индекс числа a в тестовых наборах данных"""
B = 1
"""Индекс числа b в тестовых наборах данных"""
RESULT = 2
"""Индекс результата в тестовых наборах данных"""


class TestCase(unittest.TestCase):
    """Набор тестов для проверки реализации функций расчета НОД.
    Каждый тест запускается трижды, для каждой из реализаций расчета НОД"""
    incorrect_inputs = (None, 'string', 1.1, [])
    simple_set = ((9, 3, 3),
                  (-9, 3, 3),
                  (3, 5, 1),
                  (-18, -45, 9),
                  (1, 0, 1),
                  (0, 1, 1))
    long_set = ((1005002, 1354, 2),
                (-1005002, 1354, 2),
                (65225655, 1610510, 805255),
                (-1944, -332024, 8),
                (65225655, 0, 65225655),
                (0, 65225655, 65225655))

    # def test_incorrect_first(self):
    #     """Проверка выброса исключения при передаче некорректного значения
    #     в параметр a"""
    #     err_message = 'Значение параметра a не является целым числом'
    #     for gcd in self.gcd_functions:
    #         for val in self.incorrect_inputs:
    #             self.assertRaisesRegex(Exception, err_message, gcd, val, 1)
    #
    # def test_incorrect_second(self):
    #     """Проверка выброса исключения при передаче некорректного значения
    #     в параметр b"""
    #     err_message = 'Значение параметра b не является целым числом'
    #     for gcd in self.gcd_functions:
    #         for val in self.incorrect_inputs:
    #             self.assertRaisesRegex(Exception, err_message, gcd, 1, val)
    #
    # def test_both_zero(self):
    #     """Проверка выброса исключения при передаче 0 в параметры a и b"""
    #     err_message = 'Значения параметров a и b равны нулю'
    #     for gcd in self.gcd_functions:
    #         self.assertRaisesRegex(Exception, err_message, gcd, 0, 0)

    def test_simple(self):
        """Проверка вычисления НОД на примерах небольших чисел"""
        for row in self.simple_set:
            self.assertEqual(row[RESULT], gcd(row[A], row[B]))

    def test_long(self):
        """Проверка вычисления НОД на примерах относительно больших чисел"""
        for row in self.long_set:
            self.assertEqual(row[RESULT], gcd(row[A], row[B]))


if __name__ == '__main__':
    unittest.main()
