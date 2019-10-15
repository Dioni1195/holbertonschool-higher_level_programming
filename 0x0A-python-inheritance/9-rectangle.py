#!/usr/bin/puthon3
"""This module contain an empty class """


class BaseGeometry:
    """This is a class of base geometry"""
    def area(self):
        """Calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the class"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is a class to build a rectangle

    Args:
    width(int): The width of the rectangle
    height(int): The height of the rectangle

    Attr:
    width(int): The width of the rectangle
    height(int): The height of the rectangle
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """This method calculate the area"""
        return self.__width * self.__height

    def __str__(self):
        """This is the magic method to print the object"""
        name = self.__class__.__name__
        return str("[{}] {}/{}".format(name, self.__width, self.__height))
