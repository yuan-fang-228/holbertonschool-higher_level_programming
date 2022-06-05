#!/usr/bin/python3
"""base Module"""

import json
import csv


class Base:
    """represent a class with private attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise a instance of class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dic"""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string representation of list_obj to a file"""
        newObj = []
        if list_objs is None:
            newObj = []
        else:
            for obj in list_objs:
                newObj.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(cls.to_json_string(newObj))

    @staticmethod
    def from_json_string(json_string):
        """return the list of JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 2)
            if cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, "r", encoding="utf-8") as jsonfile:
                jsonstr = jsonfile.read()
                list_dic = cls.from_json_string(jsonstr)
                for element in list_dic:
                    result.append(cls.create(**element))
                return result
        except Exception:
            return []
