#!/usr/bin/python3
''' prints the first x elements of a list and only integers '''


def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end='')
            counter += 1
        except (TypeError, ValueError):
            continue
    print()
    return counter
