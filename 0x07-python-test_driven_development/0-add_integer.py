#!/usr/bin/python3
"""This module have the function add
   it adds two numbers, they must be int or float,
   in other way a error is raised. If any number is float
   it'll convert to int. Return a int
"""


def add_integer(a, b=98):
    """Addition function
            Args: a(int), b(int)
    """
    if type(a) is not int:
        if type(a) is float:
                a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
