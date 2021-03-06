#!/usr/bin/python3
"""
    This module is about the construction of function
    that print the first a second name
"""


def say_my_name(first_name, last_name=""):
    """Print the name and the last name
    """
    x = "X name"
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
