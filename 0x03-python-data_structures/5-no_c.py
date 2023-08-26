#!/usr/bin/python3
''' Removes all characters c and C from a string '''


def no_c(my_string):
    copy_str = []
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            copy_str.append(i)
    return "".join(copy_str)
