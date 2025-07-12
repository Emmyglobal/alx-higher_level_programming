#!/usr/bin/python3
"""A function that returns a list of lists of integer"""


def pascal_triangle(n):
    """Returns a paschal's triangle"""
    my_list = [[1]]
    if n < 0:
        return []
    else:
        for i in range(1, n):
            new_row = [1]
            prev = my_list[-1]

            for j in range(1, len(prev)):
                new_row.append(prev[j - 1] + prev[j])
            new_row.append(1)
            my_list.append(new_row)
        return my_list
