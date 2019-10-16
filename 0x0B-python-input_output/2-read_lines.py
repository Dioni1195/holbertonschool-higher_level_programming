#!/usr/bin/python3
""" This module contains a function that read n lines of a file """


def number_of_lines(filename=""):
    """ Read and return the number of lines """
    with open(filename, 'r', encoding='utf-8') as r_file:
        return len(r_file.readlines())


def read_lines(filename="", nb_lines=0):
    """ Read n lines of a file """
    with open(filename, 'r', encoding='utf-8') as r_file:
        num_lines = number_of_lines(filename)
        if nb_lines <= 0 or nb_lines >= num_lines:
            print(r_file.read())
        else:
            lines = r_file.readlines()
            i = 0
            while nb_lines > 0:
                print(lines[i])
                i += 1
                nb_lines -= 1
