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

    @classmethod
    def save_to_file(cls, list_objs):
        """ This class method save a JSON to a file
        args:
        list_objs(list): List of instances who inherits of Base
        """
        new_list_obj = []
        classname = "{}{}".format(cls.__name__, ".json")
        if list_objs:
            new_list_obj = [i.to_dictionary() for i in list_objs]
        with open(classname, 'w', encoding='utf-8') as n_file:
                n_file.write(cls.to_json_string(new_list_obj))

    @staticmethod
    def from_json_string(json_string):
        """ This static method returns the list of the
        JSON string representation
        """
        new_list = []
        if json_string:
            new_list = json.loads(json_string)
        return new_list

    @staticmethod
    def to_json_string(list_dictionaries):
            """ This method converts a list to a JSON """
            if list_dictionaries is None or len(list_dictionaries) == 0:
                return json.dumps([])
            else:
                return json.dumps(list_dictionaries)
