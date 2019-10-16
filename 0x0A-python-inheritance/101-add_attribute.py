#!/usr/bin/python3
"""This module add attributes to a class"""


def add_attribute(obj, name, value):
    """This function add an attribute"""
    type_obj = type(obj)
    dict_obj = dir(type_obj)
    if "__dict__" in dict_obj:
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
