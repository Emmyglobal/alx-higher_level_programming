#!/usr/bin/python3
# A Function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for item in keys:
        print("{}: {}".format(item, a_dictionary[item]))
