#!/usr/bin/python3
"""6-load_from_json_file module"""
import json


def load_from_json_file(filename):
    """create an object from a JSON file"""
    with open(filename) as myfile:
        return json.load(myfile)
