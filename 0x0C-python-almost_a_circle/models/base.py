#!/usr/bin/python3
"""Class Base of all other classes in my project
    manage id attributes and avoid duplicating the same code
"""


class Base:
    """Base of all other classes"""
    __nb_objects = 0


    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
