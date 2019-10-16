#!/usr/bin/python3
""" This module has a function to append a string to a file """


def append_write(filename="", text=""):
    """ This function append a string """
    with open(filename, 'a', encoding='utf-8') as a_file:
        return a_file.write(text)
