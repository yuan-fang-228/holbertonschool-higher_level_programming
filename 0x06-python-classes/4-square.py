#!/usr/bin/python3
"""Represent a Square class
    Private instance attribute: size
    Instantiation with optional size
"""


class Square:
    """Represent a Square class"""
    def __init__(self, size=0):
        """Initialize the square with private instance attribute"""
        self.__size = size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the square area"""
        return self.__size * self.__size
