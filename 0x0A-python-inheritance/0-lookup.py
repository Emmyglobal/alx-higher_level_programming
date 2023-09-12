#!/usr/bin/python3
"""Returns the list of available attributes in an object"""


def lookup(obj):
    """Returns list of attributes"""
    return dir(obj)
