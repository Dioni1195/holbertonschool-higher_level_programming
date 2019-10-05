#!/usr/bin/python3
"""This module is about a function that divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function that divide each element of a matrix by div
    """
    msg_list = "matrix must be a matrix (list of lists) of integers/floats"
    msg_row = "Each row of the matrix must have the same size"
    if matrix and isinstance(matrix[0], list):
        size = len(matrix[0])
    else:
        raise TypeError(msg_list)
    if (matrix == [[]] or matrix == []) or size == 0:
        raise TypeError(msg_list)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list):
        for i in matrix:
            if isinstance(i, list):
                for j in i:
                    if len(i) != size:
                            raise TypeError(msg_row)
                    if not isinstance(j, (int, float)):
                            raise TypeError(msg_list)
            else:
                raise TypeError(msg_list)
    else:
        raise TypeError(msg_list)
    new_matrix = list(map(lambda x: list(map(
        lambda y: round(y / div, 2), x)), matrix))
    return new_matrix
