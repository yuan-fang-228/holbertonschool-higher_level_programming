#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positive_list(self):
        """test positive integer list"""
        testList = [3, 5, 7, 1, 4]
        self.assertEqual(max_integer(testList), 7)

    def test_negative_list(self):
        """test negative integer list"""
        testList = [-3, -5, -7, -1, -4]
        self.assertEqual(max_integer(testList), -1)

    def test_mix_positive_negative_list(self):
        """test mix of negative and positive integer list"""
        testList = [1, 99999, 10382, -2319482, 930847399873]
        self.assertEqual(max_integer(testList), 930847399873)

    def test_infinity_list(self):
        """test the infinity number in the list"""
        testList = [1, 5, 6574, 4352, 324, float('inf')]
        self.assertEqual(max_integer(testList), float('inf'))

    def test_two_same_max_integer(self):
        """test the two same max integer in the list"""
        testList = [123, 34, 9999, 342, 2324, 9999]
        self.assertEqual(max_integer(testList), 9999)

    def test_one_element_list(self):
        """test if there is one element in the list"""
        testList = [999]
        self.assertEqual(max_integer(testList), 999)

    def test_empty_list(self):
        """test empty list"""
        testList = []
        self.assertEqual(max_integer(testList), None)

    def test_number_string(self):
        testList = "123456789"
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_none_list(self):
        """test if test list is None"""
        testList = [None]
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_none(self):
        """test if nothing type in"""
        testList = None
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_float_list(self):
        """test the float list"""
        testList = [23.45, 234.56, 234.1, 123.4]
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_int_float_list(self):
        """test if there float and int in the list"""
        testList = [12, 234.5, 23, 456.6]
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_all_string_list(self):
        """test if all the elements are string in the list"""
        testList = ["zc", "zd", "c", "A"]
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_string_list(self):
        """test the string list will raise a typeerror exception"""
        testList = ["abc", 2, 5, 99999999]
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_invalid_type_list(self):
        """test the invalid type argument"""
        testList = {1, 34, 67, 80}
        with self.assertRaises(TypeError):
            max_integer(testList)


if __name__ == "__main__":
    unittest.main()
