#!/usr/bin/python3
""" This module contains the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ This class is to build a rectangle with different
        parameters
        args:
        __width(int): The width of the rectangle
        __height(int): The height of the rectangle
        __x(int): Position in x axis
        __y(int): Position in y axis
        id(int): Is the golbal identifier,
        public instance attribute
        attr: __width(int): The width of the rectangle
        __height(int): The height of the rectangle
        __x(int): Position in x axis
        __y(int): Position in y axis
        id(int): Is the golbal identifier,
        public instance attribute
                 """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ This property manage the width of
        the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ This property manage the height of
        the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ This property manage the position x
        of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ This property manage the position y
        of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This method calculate the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ This method prints the instance in the stdout """
        width = self.__width
        height = self.__height
        for h in range(height):
            for w in range(width):
                print("#", end="")
            print()
