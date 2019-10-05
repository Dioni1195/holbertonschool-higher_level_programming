#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """ Test cases of arguments"""
        self.assertAlmostEqual(max_integer([2, 100, -1, 12]), 100)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([-100, -2, -12]), -2)
        self.assertAlmostEqual(max_integer([-2, -2, -2]), -2)
        self.assertAlmostEqual(max_integer([0]), 0)
    def test_arg_none(self):
        """ """
        self.assertRaises(TypeError, max_integer, None)

    def test_elem_char(self):
        self.assertRaises(TypeError, max_integer, ['a', 1, 2, 3])
