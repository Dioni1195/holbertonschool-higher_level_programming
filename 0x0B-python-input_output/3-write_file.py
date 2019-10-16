#!/usr/bin/python3
""" This module has function to write a string """


def write_file(filename="", text=""):
    """This function write a string in a file """
    with open(filename, 'w', encoding='utf-8') as w_file:
        return w_file.write(text)
