#!/usr/bin/python3
"""9-student module"""


class Student:
    """define a student"""

    def __init__(self, first_name, last_name, age):
        """instantialize the class with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve a dictionary represnetation of a student instance"""
        return vars(self)
