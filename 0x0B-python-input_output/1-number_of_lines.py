#!/usr/bin/python3
""" This module has a function to returns the number of charaters
readed
"""


def number_of_lines(filename=""):
    """ Read and return the number of lines """
    with open(filename, 'r', encoding='utf-8') as r_file:
        return len(r_file.readlines())
