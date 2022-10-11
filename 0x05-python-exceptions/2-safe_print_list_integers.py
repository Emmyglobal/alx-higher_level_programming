#!/usr/bin/python3
# a function that prints the first x elements of a list and only integers
# x: input value and a new list to be printed

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            n += 1
        except (IndexError, TypeError):
            continue
    print()
    return n
