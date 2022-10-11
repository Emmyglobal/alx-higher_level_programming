#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    b = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            b += 1
        except (TypeError, ValueError):
            continue
    print()
    return b
