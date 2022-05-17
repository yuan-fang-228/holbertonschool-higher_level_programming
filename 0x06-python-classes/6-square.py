#!/usr/bin/python3
"""Represent a Square class
    Private instance attribute: size
    Private instance attribute: position
    Instantiation with optional size and optional position
    property and setter to retrieve and set it
    Public instance method: def area(self):
    Public instance method: def my_print(self):
"""


class Square:
    """Represent a Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with private instance attribute"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the square area"""
        return self.__size * self.__size

    def my_print(self):
        """ Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            if self.position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for s in range(self.__size):
                for r in range(self.__position[0]):
                    print(" ", end="")
                for c in range(self.__size):
                    print("#", end="")
                print()
