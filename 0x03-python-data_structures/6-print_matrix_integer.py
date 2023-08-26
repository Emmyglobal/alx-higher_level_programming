#!/usr/bin/python3
''' prints a matrix of integers. '''


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) != 0:
            for i in row:
                print("{:d}".format(i), end="")
                if row.index(i) != len(row) - 1:
                    print(" ", end='')
            print()
        else:
            print()
