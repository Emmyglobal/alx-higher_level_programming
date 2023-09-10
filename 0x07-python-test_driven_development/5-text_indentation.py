#!/usr/bin/python3
"""A function that prints a text"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print()
            print()
        i += 1
