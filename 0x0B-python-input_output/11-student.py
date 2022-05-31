#!/usr/bin/python3
"""11-student Module"""


class Student:
    """define a student class"""

    def __init__(self, first_name, last_name, age):
        """instantialize the class with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve a dictionary represnetation of a student instance
            if attrs is list, only retrieve the attribute names in the list
        """
        my_dict = {}
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return vars(self)
            for el in attrs:
                if hasattr(self, el):
                    my_dict[el] = getattr(self, el)
            return my_dict

        return vars(self)

    def reload_from_json(self, json):
        """replace all attributes of the student instance"""
        for key in json:
            setattr(self, key, json[key])
