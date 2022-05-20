#!/usr/bin/python3
"""0-add_integer Module
    Prototype: def add_integer(a, b=98):
        calculate the addition of 2 integers
        Return the sum
"""


def add_integer(a, b=98):
    """a function that add 2 integers
    a and b must be integers or floats, otherwise raise TypeError
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
