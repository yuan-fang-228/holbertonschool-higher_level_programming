#!/usr/bin/python3
"""12-pascal_triangle module"""


def pascal_triangle(n):
    """return a list of lists of integers representing Pascal's triangle"""
    array = [[1]]
    if n == 1:
        return array
    for row in range(0, n-1):
        li = [1]
        for col in range(0, row):
            li.append(array[-1][col] + array[-1][col + 1])
        li.append(1)
        array.append(li)

    return array
