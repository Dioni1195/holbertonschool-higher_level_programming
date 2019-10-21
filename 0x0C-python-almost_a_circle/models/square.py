#!/usr/bin/python3
""" This module contains the class of a sqaure """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class is to build a square
        Args:
            size(int): The size of the square
            x(int): The position in x axis
            y(int): The position in y axis
            id: The id of the instance
        Attrs:
            size(int): The size of the square
            x(int): The position in x axis
            y(int): The position in y axis
            id: The id of the instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)
