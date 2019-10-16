#!/usr/bin/python3
""" This module has the functon to save the json """
import json


def save_to_json_file(my_obj, filename):
    """ This function save a coded object as json
    args:
    filename(file stream): The file where the json is saved
    my_obj(object): Th python object to encode
    """
    with open(filename, 'w', encoding='utf-8') as s_file:
        json.dump(my_obj, s_file)
