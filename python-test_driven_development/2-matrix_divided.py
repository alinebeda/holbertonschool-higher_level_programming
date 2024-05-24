#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
    matrix: list of list containing int/floats
    div: number to divide matrix

    Returns:
    new matrix

    Raises:
        TypeError: if matrix is not a list of the lists
        TypeError: if rows are not the same size
        TypeError: if div is neither int nor float
        ZeroDivisionError: when div is zero
    """
    matrix_reloaded = []
    row_length = 0
    list_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not (isinstance(matrix, list) or isinstance(matrix[0], list)
            or len(matrix[0]) <= 0):
        raise TypeError(list_error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        new_row = []
        if row_length == 0:
            row_length = len(row)
        elif not (len(row) == row_length):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(list_error)
            new_row.append(round(num / div, 2))
        matrix_reloaded.append(new_row)
    return matrix_reloaded
