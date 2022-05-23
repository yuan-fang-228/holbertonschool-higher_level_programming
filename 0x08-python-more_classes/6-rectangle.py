#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """represent a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize the rectangle with width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calculate the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """calculate the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """return the rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        rec = ""
        for i in range(self.height):
            for j in range(self.width):
                rec = rec + "#"
            if i != self.height - 1:
                rec = rec + "\n"
        return rec

    def __repr__(self):
        """return a string representation of the rectangle"""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """delete the instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
