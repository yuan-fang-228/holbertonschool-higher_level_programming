#!/usr/bin/python3
"""7-base_geometry Module"""


class BaseGeometry:
    """represent a class"""

    def area(self):
        """raise an exception with message
            "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """valid the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
