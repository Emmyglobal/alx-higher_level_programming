#!/usr/bin/python3
"""A function that reads a text file with utf-8 encoding"""

def read_file(filename=""):
    with open(filename, mode='r', encoding="utf-8") as f:
        text = f.read()
    print(text)
