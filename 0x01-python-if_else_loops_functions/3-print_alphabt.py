#!/usr/bin/python3
''' print all alphabets except q and e '''

for i in range(97, 123):
    if i != 113 and i != 101:
        print("{}".format(chr(i)), end="")
