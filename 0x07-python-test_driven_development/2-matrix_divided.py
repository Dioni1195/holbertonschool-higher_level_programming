#!/usr/bin/python3
"""This module is about a function that divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    size = len(matrix[0])
    if isinstance(div, (int, float)) == False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list):
        for i in matrix:
            if isinstance(i, list):
                for j in i:
                    if len(i) != size:
                            raise TypeError("Each row of the matrix must have the same size")
                    if type(j) is not int and type(j) is not float:
                            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return new_matrix
