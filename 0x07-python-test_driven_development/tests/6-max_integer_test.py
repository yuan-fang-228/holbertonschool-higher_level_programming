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

    def test_max_at_head(self):
        """test if max number is at beginnng of the list"""
        testList = [8, 8, 8, 7, 2]
        self.assertEqual(max_integer(testList), 8)

    def test_same_number_list(self):
        """test if all the numbers in the list are the same"""
        testList = [6, 6, 6, 6]
        self.assertEqual(max_integer(testList), 6)

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
        self.assertEqual(max_integer(testList), "9")

    def test_none_list(self):
        """test if test list is None"""
        testList = [None]
        self.assertEqual(max_integer(testList), None)

    def test_dict(self):
        """test if it is a dictionary"""
        testList = [{1, 2}, {3, 4, 5}]
        self.assertEqual(max_integer(testList), {1, 2})

    def test_none(self):
        """test if nothing type in"""
        testList = None
        with self.assertRaises(TypeError):
            max_integer(testList)

    def test_float_list(self):
        """test the float list"""
        testList = [23.45, 234.56, 234.1, 123.4]
        self.assertEqual(max_integer(testList), 234.56)

    def test_int_float_list(self):
        """test if there float and int in the list"""
        testList = [12, 234.5, 23, 456.6]
        self.assertEqual(max_integer(testList), 456.6)

    def test_all_string_list(self):
        """test if all the elements are string in the list"""
        testList = ["zc", "zd", "c", "A"]
        self.assertEqual(max_integer(testList), "zd")

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
