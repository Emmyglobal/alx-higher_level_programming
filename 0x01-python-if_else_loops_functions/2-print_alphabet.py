#!/usr/bin/python3
"""print the alphabet in lowercase, not followed by a new line"""
for letters in range(97, 123):
    print("{}".format(chr(letters)), end="")
