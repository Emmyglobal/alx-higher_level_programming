#!/usr/bin/python3
def print_last_digit(number):
    for i in range(number):
        print("{}".format(abs(number) % 10))
