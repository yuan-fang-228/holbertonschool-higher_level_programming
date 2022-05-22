#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_list(self):
        """test positive integer list"""
        list = [3, 5, 7, 1, 4]
        self.assertEqual(max_integer(list), 7)

    def test_negative_list(self):
        """test negative integer list"""
        list = [-3, -5, -7, -1, -4]
        self.assertEqual(max_integer(list), -1)

    def test_mix_positive_negative_list(self):
        """test mix of negative and positive integer list"""
        list = [1, 99999, 10382, -2319482, 930847399873]
        self.assertEqual(max_integer(list), 930847399873)

    def test_infinity_list(self):
        """test the infinity number in the list"""
        list = [1, 5, 6574, 4352, 324, float('inf')]
        self.assertEqual(max_integer(list),float('inf'))

    def test_two_same_max_integer(self):
        """test the two same max integer in the list"""
        list = [123, 34, 9999, 342, 2324, 9999]
        self.assertEqual(max_integer(list), 9999)

    def test_one_element_list(self):
        """test if there is one element in the list"""
        list = [999]
        self.assertEqual(max_integer(list), 999)

    def test_empty_list(self):
        """test empty list"""
        list = []
        self.assertEqual(max_integer(list),None)
