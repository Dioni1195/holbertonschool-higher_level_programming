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
            self.size = __size

    @property
    def size(self):
            """Property Size, the size of the square"""
            return self.__size

    @size.setter
    def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """It calcule the area of a square

            Returns:
                The area of square, an int.

        """
        return self.__size ** 2

    def my_print(self):
        """It prints the square.

            Returns:
                Nothing.

        """
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(size):
                for i in range(size):
                    print('#', end="")
                print()
