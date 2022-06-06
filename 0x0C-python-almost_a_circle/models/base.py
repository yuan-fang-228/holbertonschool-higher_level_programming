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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialiation - convert it to csv string and save in the file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributename = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    attributename = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=attributename)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserialiation - load a list of object from csv file"""
        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    attributename = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    attributename = ["id", "size", "x", "y"]
                dictreader = csv.DictReader(csvfile, fieldnames=attributename)
                for item in dictreader:
                    item = {k: int(v) for k, v in item.items()}
                    list_objs.append(cls.create(**item))
                return list_objs
        except Exception:
            return list_objs
