#!/usr/bin/python3
"""10-square Module"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """this square class inherits from Rectangle"""

    def __init__(self, size):
        """initialise the instance of square"""
        super().__init__(size, size)
