#!/usr/bin/python3
"""Prints the ASCII alphabet, in reverse order"""

for i in range(122, 97 - 1, -1):
    if (i % 2) != 0:
        j = chr(i).upper()
    else:
        j = chr(i)
    print("{}".format(j), end="")
