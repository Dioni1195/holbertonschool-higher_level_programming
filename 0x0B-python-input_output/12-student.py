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
        for verify in attrs:
            if verify in self.__dict__.keys():
                new_dict[verify] = self.__dict__[verify]
        return new_dict
