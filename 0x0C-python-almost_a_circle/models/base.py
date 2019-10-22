#!/usr/bin/python3
""" This module containtes the class base """
import json


class Base:
    """ This class will be used in all of the next classes
        args:
        id(int): Is the golbal identifier,
        public instance attribute
        attr:
        __nb_objects(int): Is the number of the objects of the class
        id(int): Is the golbal identifier,
        public instance attribute
                 """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
            """ This method converts a list to a JSON """
            if list_dictionaries is None or len(list_dictionaries) == 0:
                return []
            else:
                return json.dumps(list_dictionaries)
