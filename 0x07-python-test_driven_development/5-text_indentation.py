#!/usr/bin/python3
"""
The Function prints a text with 2 new libes after each of these
characters: '.', '?' and ':'
"""


def text_indentation(text):
    """Returns a text with new line after special chars

    Args:
        text
    """
    if (not isinstance(text, str)):
        raise TypeError('text must be a string')
    i = 0
    for char in text:
        if i == 0:
            if char == ' ':
                continue
            else:
                i = 1
        if i == 1:
            if char in ".?:":
                print(char)
                print()
                i = 0
            else:
                print(char, end="")
