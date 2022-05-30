#!/usr/bin/python3
"""4-inherits_from Module"""


def inherits_from(obj, a_class):
    """return True if an object is an instance of a class
        that inherited from the specified class otherwise return False"""
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
