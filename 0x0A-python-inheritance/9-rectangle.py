#!/usr/bin/python3
"""9-rectangle Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialise the instance of class rectangle with width and height
            width and weith to be valid"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """formate the print of this instance of Rectangle"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
