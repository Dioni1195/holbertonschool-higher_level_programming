#!/usr/bin/python3
""" This module define a class Student """


class Student:
    """ This is a class for a student
    args:
    first_name(str): The first name of the student
    last_name(str): The last name of th student
    age(int): The age of the student
    attrs:
    first_name(str): The first name of the student
    last_name(str): The last name of th student
    age(int): The age of the student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary
        representation of the class
        """
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        for verify in self.__dict__.keys():
            if verify in attrs:
                new_dict[verify] = verify
        return new_dict

    def reload_from_json(self, json):
        """ Reload the attributes from json
        args:
        json(dict): The dict from to reload
        """
        if len(json) != 0:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
