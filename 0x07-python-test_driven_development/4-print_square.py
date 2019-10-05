#!/usr/bin/python3
"""
    This module has a function that prints a square
"""


def print_square(size):
    """
       This function takes a argument and print a square
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
