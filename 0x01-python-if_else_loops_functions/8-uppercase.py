#!/usr/bin/python3
''' prints a string in uppercase followed by a new line '''

def uppercase(str):
    for i in str:
        num = ord(i)
        if num >= 97 and num < 124:
            num = num - 32
        print("{}".format(chr(num)), end="")
    print()
