#!/usr/bin/python3
"""Represent a square class
    Private instance attribute: size
    Instantiation with size
    Public instance method: def area(self)
    Square instance can answer to comparators ==, !=, >, >=, < and <=
"""


class Square:
    """Represent a square class"""
    def __init__(self, size=0):
        """Instantiation the square with size"""
        self.size = size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size value"""
        if type(value) is not int:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate the current square area"""
        return self.size ** 2

    def __eq__(self, other):
        """define == to compare with current square area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define != to compare with current square area"""
        return self.area() != other.area()

    def __gt__(self, other):
        """define > to compare with current square area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define >= to compare with current square area"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """define < to compare with current square area"""
        return self.area() < other.area()

    def __le__(self, other):
        """define <= to compare with current square area"""
        return self.area() <= other.area()
