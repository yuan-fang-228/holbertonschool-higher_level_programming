#!/usr/bin/python3
"""8-class_to_json module"""


def class_to_json(obj):
    """return a dictionary description with simple data structure"""
    return vars(obj)
