#!/usr/bin/python3
"""
Creating the first class which is the base class
"""


class Base:
    """
    Args: id
    The base class with the init method including setter and getter
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of the class
        Args: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
