#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_common_case(self):
        """ Test normal arguments"""
        self.assertAlmostEqual(max_integer([2, 100, -1, 12]), 100)

    def test_no_args(self):
        """ Test without arguments"""
        self.assertAlmostEqual(max_integer(), None)

    def test_empty(self):
        """ Test empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    def test_first_max(self):
        """ Test first is the max"""
        self.assertAlmostEqual(max_integer([100, 2, 50]), 100)

    def test_last_max(self):
        """ Tests the last one is the max"""
        self.assertAlmostEqual(max_integer([100, 2, 500]), 500)

    def test_negative(self):
        """ Test negative arguments"""
        self.assertAlmostEqual(max_integer([-100, -2, -12]), -2)

    def test_times(self):
        """ Test many times max arguments"""
        self.assertAlmostEqual(max_integer([-2, -2, -200]), -2)

    def test_tuple(self):
        """Test tuple as argument"""
        self.assertAlmostEqual(max_integer((2, 3, 0)), 3)

    def test_floats(self):
        """Floats as Arguments"""
        self.assertAlmostEqual(max_integer([2.3, -2.3, 1.5]), 2.3)

    def test_float_int(self):
        """Floats and ints as arguments"""
        self.assertAlmostEqual(max_integer([2.3, 3, 1.5]), 3)

    def test_tuples_elem(self):
        """Tuples as elements of the list"""
        self.assertAlmostEqual(max_integer([(2.3, 3), (1.5, 2)]), (2.3, 3))

    def test_tup_flo_int(self):
        """Tuples, floats and ints as parameters"""
        self.assertRaises(TypeError, max_integer, [(1, 2), 2, 3.4])

    def test_zero(self):
        """ Test zero as argument"""
        self.assertAlmostEqual(max_integer([0]), 0)

    def test_arg_none(self):
        """None as argument error"""
        self.assertRaises(TypeError, max_integer, None)

    def test_elem_char(self):
        """Parameter as set"""
        self.assertRaises(TypeError, max_integer, {1, 2, 3})

    def test_elem_char(self):
        """An element no int"""
        self.assertRaises(TypeError, max_integer, ['a', 1, 2, 3])

    def test_char(self):
        """Test all elements chars"""
        self.assertAlmostEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_string(self):
        """Test string as argument"""
        self.assertAlmostEqual(max_integer("abc"), 'c')
