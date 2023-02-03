#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = [i for i in matrix]
    copy = [x * x for y in copy for x in y]
    return copy
