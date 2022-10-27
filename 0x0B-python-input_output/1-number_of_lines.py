#!/usr/bin/python3
#1-number_of_lines.py

def nuber_of_lines(filename) as f:
    lines = 0
    with open(filename) as f:
        for line in f:
            line += 1
    return lines
