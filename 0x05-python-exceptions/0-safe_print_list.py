#!/usr/bin/python3

# A function that prints x elements of a list
# x : The number of elements to print

def safe_print_list(my_list=[], x=0):
    n = 0
    for n in my_list:
        x += 1

    try:
        for x in my_list:
            print(my_list[x], end="")
    except (IndexError):
        print()
        return(x)
