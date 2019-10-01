#!/usr/bin/python3
"""This module contains the class Square
"""


class Square:
    """Class square to make a matrix
       Args:
        __size (int): The size of the square
       Attributes:
        __size (int): The size of the square

    """
    def __init__(self, __size=0):
            if type(__size) is not int:
                raise TypeError("size must be an integer")
            if __size < 0:
                raise ValueError("size must be >= 0")
            self.__size = __size
