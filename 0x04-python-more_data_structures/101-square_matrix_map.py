#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x * x, matrix[0])), list(map(lambda y: y * y, matrix[1])), list(map(lambda z: z * z, matrix[2]))]
