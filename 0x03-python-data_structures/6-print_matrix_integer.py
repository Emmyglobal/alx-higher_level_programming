#!/usr/bin/python3
''' prints a matrix of integers '''


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix) - 1):
        for j range(len(matrix) - 1):
            print("{}".format(matrix[i][j]))
