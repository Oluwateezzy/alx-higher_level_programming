#!/usr/bin/python3
def matrix_divided(matrix, div):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by Zero")
    
    return list(map(lambda x: list(map(lambda y: y / div, x)), matrix))
