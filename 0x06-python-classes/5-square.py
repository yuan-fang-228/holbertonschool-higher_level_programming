#!/usr/bin/python3
"""Represent a Square class
    Private instance attribute: size
    Instantiation with optional size
    property and setter to retrieve and set it
    Public instance method: def area(self):
    Public instance method: def my_print(self):
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

    def my_print(self):
        """print in stdout the square with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
