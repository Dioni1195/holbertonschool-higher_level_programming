#!/usr/bin/python3
""" This module is about how read a file """


def read_file(filename=""):
    """ This function opens and read a file """
    with open(filename, 'r', encoding='utf-8') as r_file:
        print(r_file.read())
