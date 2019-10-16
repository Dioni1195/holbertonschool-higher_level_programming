#!/usr/bin/python3
""" This module load a json from file """
import json


def load_from_json_file(filename):
    """ This function load a json from a file
    args:
    filename(file stream): The file where the json is stored
    """
    with open(filename, 'r', encoding='utf-8') as j_file:
        return json.load(j_file)
