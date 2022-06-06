#!/usr/bin/python3
""" Contains tests for class Square"""


import unittest
import inspect
import pycodestyle

from models import square
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.square_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """ Test for functionality of class"""

    def test_update_number_of_args(self):
        """ Test update method with number of arguments passed in"""
        sq = Square(5, 5, 5, 5)
        sq.update()
        self.assertEqual(str(sq), "[Square] (5) 5/5 - 5")
        sq1 = Square(11)
        sq1.update(1, 1, 1, 1, 1)
        self.assertEqual(str(sq1), "[Square] (1) 1/1 - 1")

    def test_update_normal_args_kwargs(self):
        """test update method with normal args and kwwargs"""
        sq = Square(5)
        sq.update(10)
        self.assertEqual(str(sq), "[Square] (10) 0/0 - 5")
        sq.update(1, 2)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 2")
        sq.update(1, 2, 3)
        self.assertEqual(str(sq), "[Square] (1) 3/0 - 2")
        sq.update(1, 2, 3, 4)
        self.assertEqual(str(sq), "[Square] (1) 3/4 - 2")
        sq1 = Square(10)
        sq1.update(id=1)
        self.assertEqual(str(sq1), "[Square] (1) 0/0 - 10")
        sq1.update(id=1, size=7)
        self.assertEqual(str(sq1), "[Square] (1) 0/0 - 7")
        sq1.update(id=1, size=7, x=8)
        self.assertEqual(str(sq1), "[Square] (1) 8/0 - 7")
        sq1.update(id=1, size=7, x=8, y=9)
        self.assertEqual(str(sq1), "[Square] (1) 8/9 - 7")

    def test_update_have_both_args_kwargs(self):
        """test update method both args and kwargs passed in"""
        sq = Square(1, 2, 3, 4)
        sq.update(5, id=6)
        self.assertEqual(str(sq), "[Square] (5) 2/3 - 1")
        sq.update(5, id=6, x=7)
        self.assertEqual(str(sq), "[Square] (5) 2/3 - 1")

    def test_update_invalid_attribute(self):
        """test update method with invalid attributes"""
        sq = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update("aa", "bb", 5, 6)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(5, 6, "aa", "bb")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(1, "aa", 5, 6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(1, 3, 5, "aa")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(1, 3, 5, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(5, 6, -2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(5, -6, 3, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size="size")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x="x")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y="y")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(y="y", x="x")

    def test_dictionary_with_normal_args(self):
        """test to dictionary method with normal args"""
        s1 = Square(10, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {"id": 4, "size": 10, "x": 2, "y": 3})
        self.assertEqual(dict, type(s1_dictionary))
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(s2_dictionary, s1_dictionary)
        self.assertEqual(dict, type(s2_dictionary))

    def test_dictionary_with_invalid_args(self):
        s1 = Square(10, 2, 1)
        errmsg = 'to_dictionary() takes 1 positional argument but 2 were given'
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary({"id": 1, "x": 1, "y": 1})
