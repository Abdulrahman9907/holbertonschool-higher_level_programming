#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -1]), -1)

    def test_mixed_numbers(self):
        """Test with mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1, 2]), 2)
        self.assertEqual(max_integer([10, -5, 0, 15]), 15)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_max_at_beginning(self):
        """Test with maximum at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test with maximum at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_max_in_middle(self):
        """Test with maximum in the middle"""
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_all_same_numbers(self):
        """Test with all same numbers"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 1.8]), 2.7)

    def test_zero_in_list(self):
        """Test with zero in the list"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-1, 0, -2]), 0)


if __name__ == '__main__':
    unittest.main()