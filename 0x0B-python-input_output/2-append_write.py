#!/usr/bin/python3
"""
 function that appends a string at the end of a text
 file (UTF8) and returns the number of characters added:
 """


def append_write(filename="", text=""):
    """appends and returns number of characters added"""
    with open(filename, 'a', encoding='utf-8') as apen:
        return apen.write(text)
