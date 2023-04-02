#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    This function diveides matrix values by div

    Args:
    matrix: list of lists
    div (int): value to be divided by

    Returns:
    the new matrix
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(row, list) and all(isinstance(elements, (int, float))for elements in row)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return(new_matrix)
