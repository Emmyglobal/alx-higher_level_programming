#!/usr/bin/python3
''' Removes all characters c and C from a string '''


def no_c(my_string):
    for i in range(len(my_string)-1):
        if my_string[i] == 99 or my_string[i] == 67:
            return my_string.pop(idx)
