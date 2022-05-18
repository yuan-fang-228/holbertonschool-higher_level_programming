#!/usr/bin/python3
"""define a MagicClass with 3 functions"""


import math
class MagicClass:
    """represent a circle"""
    def __init__(self, radius=0):
        """initialize the magicclass with radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """calculate the area"""
        return (self.radius ** 2 * math.pi)

    def circumference(self):
        """calculate the circumference"""
        return (2 * math.pi * self.__radius)
