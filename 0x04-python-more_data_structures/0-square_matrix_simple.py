#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[for j in range(len(matrix[i]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[i][j] = matrix[i][j] ** 2

    return (result)
