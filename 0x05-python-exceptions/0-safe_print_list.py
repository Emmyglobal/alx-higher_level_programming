#!/usr/bin/python3

# A function that prints x elements of a list
# x : The number of elements to print

def safe_print_list(my_list=[], x=0):
    n = 0
    for j in my_list:
        n += 1

    try:
        for k in range(x):
            print(my_list[k], end="")
        print()
        return x
    except (IndexError):
        print()
        return n
