#!/usr/bin/python3
""" This module has a function to determinate the
class of an object
"""


def is_same_class(obj, a_class):
    """This function return True if obj is an object of the class a_class"""
    if type(obj) == a_class:
        return True
    else:
        return False
