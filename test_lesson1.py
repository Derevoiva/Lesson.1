"""Unit tests for the corrected Lesson 1 solutions."""
import unittest

from lesson1 import (
    business_result, format_seconds, largest_digit,
    repeated_digit_sum, running_target_day,
)


class Lesson1Tests(unittest.TestCase):
    def test_format_seconds(self):
        self.assertEqual(format_seconds(0), "00:00:00")
        self.assertEqual(format_seconds(3661), "01:01:01")
        self.assertEqual(format_seconds(90000), "25:00:00")
        with self.assertRaises(ValueError):
            format_seconds(-1)

    def test_repeated_digit_sum(self):
        self.assertEqual(repeated_digit_sum(3), 369)
        self.assertEqual(repeated_digit_sum(0), 0)
        with self.assertRaises(ValueError):
            repeated_digit_sum(12)

    def test_largest_digit(self):
        self.assertEqual(largest_digit(0), 0)
        self.assertEqual(largest_digit(-9062), 9)

    def test_business_result(self):
        result = business_result(100, 80, 4)
        self.assertEqual(result["profit"], 20)
        self.assertAlmostEqual(result["margin"], 0.2)
        self.assertEqual(result["profit_per_employee"], 5)
        self.assertEqual(business_result(10, 10)["status"], "break-even")
        with self.assertRaises(ValueError):
            business_result(100, 80, 0)

    def test_running_target_day(self):
        self.assertEqual(running_target_day(5, 5), 1)
        self.assertEqual(running_target_day(5, 5.5), 2)
        with self.assertRaises(ValueError):
            running_target_day(0, 5)


if __name__ == "__main__":
    unittest.main()
