#!/usr/bin/python3
# A Function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):

    return([list(map(lambda data: data * data, row))for row in matrix])
