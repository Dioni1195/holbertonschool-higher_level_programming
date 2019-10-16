#!/usr/bin/python3
"""A rebel class of int"""


class MyInt(int):
    """This class inherits from int but is rebel"""
    def __eq__(self, other):
        """ The equal method """
        return int(self) != int(other)

    def __ne__(self, other):
        """ The different method """
        return int(self) == int(other)
