#!/usr/bin/python3
"""
Function that multiplies two matricess
"""


def matrix_mul(m_a, m_b):
    """
    multiplication of m_a and m_b
    Args:
        m_a: the first matrix
        m_b: the second matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_a must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix1 = []
    for i in range(len(m_b[0])):
        my_row = []
        for j in range(len(m_b)):
            my_row.append(m_b[j][i])
        matrix1.append(my_row)

    matrix2 = []
    for row in m_a:
        my_row = []
        for column in matrix1:
            product = 0
            for m in range(len(matrix1[0])):
                product += row[m] * column[m]
            my_row.append(product)
        matrix2.append(my_row)

    return matrix2
