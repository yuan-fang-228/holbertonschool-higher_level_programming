#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """check if object is an instance of the specified class
        or that class inherited from"""
    if isinstance(obj, a_class):
        return True
    return False
