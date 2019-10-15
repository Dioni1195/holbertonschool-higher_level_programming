#!/usr/bin/python3
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
