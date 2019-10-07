#!/usr/bin/python3
""" This module is about a class to generate a rectangle"""


class Rectangle:
    """This is a class to generate a rectangle
       Args:
        __width(int): The width of the rectangle
        __height(int): The height of the rectangle

       Attributes:
       __width(int): The width of the rectangle
       __height(int): The height of the rectangle

     """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ This property is the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """This is the property for the height argument"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """This method return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """This method return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """This is the magic method to return a printeable method"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ["#" * self.__width + '\n'] * self.__height
        str_rec = ""
        for i in rec:
            str_rec += str(i)
        return str_rec[0:-1]
