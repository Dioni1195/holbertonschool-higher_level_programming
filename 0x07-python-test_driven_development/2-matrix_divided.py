#!/usr/bin/python3
"""This module is about a function that divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    size = len(matrix[0])

    new_matrix = [['a'] * size]* len(matrix)
    print(new_matrix)
    column = 0
    row = 0
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is list:
        for i in matrix:
            for j in i:
                if len(i) is not size:
                        raise ("Each row of the matrix must have the same size")
                if type(j) is not int and type(j) is not float:
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                new_matrix[row][column]
                column += 1
            row += 1
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return new_matrix
