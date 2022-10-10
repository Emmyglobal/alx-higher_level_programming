#!/usr/bin/python3

# A function that prints x elements of a list
# x : The number of elements to print

def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list:
            print("{}".format(my_list[x]), end="")
    except (ValueError, TypeError):
        return(x)
