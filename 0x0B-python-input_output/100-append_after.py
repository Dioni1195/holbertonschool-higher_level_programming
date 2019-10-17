#!/usr/bin/python3
""" This module contain a function that append a line after other """


def append_after(filename="", search_string="", new_string=""):
    """ This function append a line after other """
    with open(filename, 'r+', encoding='utf-8') as r_file:
        r_str = r_file.readlines()
        appended_str = []
        for search in r_str:
            appended_str.append(search)
            if search.find(search_string) != -1:
                appended_str.append(new_string)
        with open(filename, 'w', encoding='utf-8') as w_file:
            w_file.writelines(appended_str)
