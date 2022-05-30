#!/usr/bin/python3
"""11-square Module"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """inherit from Rectangle"""

    def __init__(self, size):
        """initialise the instance of square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
