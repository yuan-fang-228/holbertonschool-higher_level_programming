#!/usr/bin/python3
"""2-matrix_divided Module
    prototype: def matrix_divided(matrix, div):
            divide all the elements of the matrix
            Return a new matrix with the result
"""


def matrix_divided(matrix, div):
    """a function that divide each element by div
        result to be rounded to 2 decimal places
        put results in a new matrix and return the new matrix"""

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    length = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for el in row:
            if type(el) is not int and type(el) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_row.append(round(el/div, 2))
        new_matrix.append(new_row)
    return new_matrix
