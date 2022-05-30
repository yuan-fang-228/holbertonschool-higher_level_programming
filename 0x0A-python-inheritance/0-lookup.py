#!/usr/bin/python3
"""define a function that find all the attributes and methods of an object"""


def lookup(obj):
    """return a list of available attributes and methods of one object"""
    return (dir(obj))
