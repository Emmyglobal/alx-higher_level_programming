#!/usr/bin/python3
def print_last_digit(number):
    if (abs(number) >= 0):
        print("{}".format(abs(number) % 10), end="")
    else:
        print("-{}".format(abs(number) % 10), end="")
