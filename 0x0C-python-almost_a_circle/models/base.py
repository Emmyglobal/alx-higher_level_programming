#!/usr/bin/python3
"""the first class"""


class Base:
    __nb_objects = 0

    """A class constructor"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
