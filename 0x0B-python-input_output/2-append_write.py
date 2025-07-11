#!/usr/bin/python3
"""A function that appends a strink at the end of a text file"""


def append_write(filename="", text=""):
    """appends and returns the number of character added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
