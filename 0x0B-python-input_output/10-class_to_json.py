#!/usr/bin/python3
""" This module contains a function that convert a class
to JSON and then to dict
"""


def class_to_json(obj):
    """ This function convert a clas to json """
    return obj.__dict__
