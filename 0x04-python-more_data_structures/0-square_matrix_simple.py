#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat1 = []
    for x in matrix:
        mat2 = []
        for y in x:
             mat2.append(y ** 2)
        mat1.append(mat2)
    return mat1
