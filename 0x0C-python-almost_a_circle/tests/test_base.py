#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pycodestyle

from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """ Tests functionality of class"""

    def setUp(self):
        """Reset nb_object to 0 for every test"""
        Base._Base__nb_objects = 0

    def test_id_none(self):
        """ Tests id as none"""
        b_1 = Base()
        self.assertEqual(b_1.id, 1)

    def test_id_assigned(self):
        """ Tests id is give"""
        b_2 = Base(8)
        self.assertEqual(b_2.id, 8)

    def test_too_many_args(self):
        """ Tests entering too many args to instantiate class"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_increment_if_none_id(self):
        """Test increment if id is None """
        b_0 = Base()
        self.assertEqual(b_0.id, 1)
        b_1 = Base()
        self.assertEqual(b_1.id, 2)
        b_2 = Base()
        self.assertEqual(b_2.id, 3)

    def test_increment_id_with_value_none_comb(self):
        """Test increment if id is none or with value"""
        b_0 = Base()
        self.assertEqual(b_0.id, 1)
        b_1 = Base(-1)
        self.assertEqual(b_1.id, -1)
        b_2 = Base(-10)
        self.assertEqual(b_2.id, -10)
        b_3 = Base()
        self.assertEqual(b_3.id, 2)
        b_4 = Base()
        self.assertEqual(b_4.id, 3)
        b_5 = Base(10)
        self.assertEqual(b_5.id, 10)
