#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a
    if len(tuple_b) == 1:
        x, = tuple_b
        new_tuple = (a + x, b + 0)
    elif len(tuple_b) == 0:
        return tuple_a
    else:
        x, y = tuple_b
        new_tuple = (a + x, b + y)
    return new_tuple
