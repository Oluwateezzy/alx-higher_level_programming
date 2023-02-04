#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = matrix.copy()

    for i in range(len(matrix)):
        copy[i] = list(map(lambda x: x ** 2, matrix[i]))
    return (copy)
