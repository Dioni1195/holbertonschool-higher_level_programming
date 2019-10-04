#!/usr/bin/python3
"""
"""


def say_my_name(first_name, last_name=""):
    """
    """
    x = "X name"
    if not isinstance(first_name, str) or isinstance(last_name, str) == False:
        raise TypeError("{} must be a string".format(x))
    print("My name is {} {}".format(first_name, last_name))
