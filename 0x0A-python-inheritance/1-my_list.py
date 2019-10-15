#!/usr/bin/python3
""" This module contains a inheritance class"""


class MyList(list):
    """This class inherate from list class
    and contain a method to sort a list"""

    def print_sorted(self):
        """This method print a sorted list"""
        new_list = self.copy()
        print(sorted(new_list))
