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

    def area(self):
        """It calcule the area of a square

            Returns:
                The area of square, an int.

        """
        return self.__size ** 2
