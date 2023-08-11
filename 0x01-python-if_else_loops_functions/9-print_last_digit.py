#!/usr/bin/python3
''' prints last colour '''


def print_last_digit(number):
    r = abs(number) % 10
    print("{}".format(r), end="")
    return (r)
