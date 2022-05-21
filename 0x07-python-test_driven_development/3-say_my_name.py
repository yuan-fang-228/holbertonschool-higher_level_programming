#!/usr/bin/python3
"""3-say_my_name Module
    Prototype: def say_my_name(first_name, last_name=""):
    Print first name and last name
    First name and last name number string
"""


def say_my_name(first_name, last_name=""):
    """a function that prints fist name and last name
        fist name and last name must be string
        otherwise TypeError will be raised"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
