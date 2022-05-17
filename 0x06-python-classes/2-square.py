#!/usr/bin/python3
"""Represent a Square class
    Private instance attribute: size
    Instantiation with optional size
"""


class Square:
    """Represent a Square class"""
    def __init__(self, size=0):
        """Initialize the square with private instance attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
