#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:  # open the file
        for line in r:  # loop through lines
            text += line  # append the lines to variable `text`
            if search_string in line:  # check if search string is present in a line
                text += new_string  # append the new string to the text
    with open(filename, "w") as w:  # open the file
        w.write(text)  # write the text to the file
