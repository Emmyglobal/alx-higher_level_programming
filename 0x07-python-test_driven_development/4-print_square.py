#!/usr/bin/python3
"""A function that prints a square"""


def print_square(size):
    """Prints a square with character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif (type(size) == float) and (size < 0):
        raise TypeError("size must be an integer")
    elif size == 0:
        pass
    else:
        for i in range(size ** 2):
            if i and not(i % size):
                print()
            print(f'#', end="")
        print()
