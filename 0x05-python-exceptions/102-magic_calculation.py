#!/usr/bin/python3
def magic_calculation(a, b):
    add = a + b
    sub = a - b
    try:
        if a < b:
            c = add(a, b)
            for i in range(a, b):
                c = add(c, i)
        return c
    except (TypeError, ValueError):
        return sub(a, b)
