#!/usr/bin/python3
''' prints a matrix of integers '''


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if row:
                print("{:d} {:d} {:d}".format(row[0], row[1], row[2]))
            else:
                print()
