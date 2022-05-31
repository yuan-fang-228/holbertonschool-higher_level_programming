#!/usr/bin/python3
"""5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """write object to a text file using JSON represnetation"""
    with open(filename, "w", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
