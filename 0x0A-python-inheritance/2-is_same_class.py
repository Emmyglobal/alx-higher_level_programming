#!/usr/bin/python3
"""Returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """True if exactly an instance of the specified class ; otherwise False."""
    return isinstance(obj) is a_class
