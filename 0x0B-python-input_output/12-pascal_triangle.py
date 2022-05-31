#!/usr/bin/python3
"""12-pascal_triangle module"""


def pascal_triangle(n):
    """return a list of lists of integers representing Pascal's triangle"""
    if n < 0:
        return []
    array = []
    for row in range(0, n):
        array.append([])
        array[row].append(1)
        for col in range(1, row):
            array[row].append(array[row-1][col-1] + array[row-1][col])
        if (row != 0):
            array[row].append(1)

    return array
