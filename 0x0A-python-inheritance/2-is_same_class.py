#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """return True if it is an instance of specified class
        otherwise return False"""
    if type(obj) is a_class:
        return True
    return False
