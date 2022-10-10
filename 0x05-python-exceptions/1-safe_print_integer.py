#!/usr/bin/python3
#Write a function that prints an integer with "{:d}".format()

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        return False
    else:
        return True

safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value)
