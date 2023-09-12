#!/usr/bin/python3
"""
The "7-base_geometry" module
"""


class BaseGeometry:
    """
    A class with two public instance methods;
    @area: raises an Exception
    @integer_validator: raises Type and Value Error.
    """
    def __init__(self):
        """Initialisation"""

    def area(self):
        """Area that raise an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks the parameter and raises
        TypeError and ValueError if conditions aren't met
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
