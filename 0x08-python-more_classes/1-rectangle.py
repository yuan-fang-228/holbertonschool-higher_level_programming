#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle with width and height"""
        self.height = height
        self.width = width

    def checkInt(self, value, attributeName):
        """check whether the attribute is integer or not"""
        if type(value) is not int:
            raise TypeError(f"{attributeName} must be an integer")
        if value < 0:
            raise ValueError(f"{attributeName} must be >= 0")

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width value"""
        self.checkInt(value, "width")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height value"""
        self.checkInt(value, "height")
        self.__height = value
