#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherite\
        (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """returns True or False"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
