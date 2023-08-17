#!/usr/bin/python3
# A Function that returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
