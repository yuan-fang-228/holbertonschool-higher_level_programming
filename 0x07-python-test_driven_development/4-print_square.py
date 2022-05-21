#!/usr/bin/python3
"""4-print_square Module
    Prototype: def print_square(size):
        Print a square with the character #
        size is the size length of the square
"""


def print_square(size):
    """a function that prints a # square
        size must be an integer, otherwise raise TypeError
        size must be >= 0, otherwise raise ValueError"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
