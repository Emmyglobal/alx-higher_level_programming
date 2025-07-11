#!/usr/bin/python3
"""A function that writes a string to a text file(UTF8)"""


def write_file(filename="", text=""):
    """returns the number of character written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
