#!/usr/bin/python3
"""a function that adds a new attribute to an object if it's possible"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible
    
    Args:
        obj: The object to which the attribute will be added.
        name (str): The name of the new attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object doesn't suppot dynamic attribute ass.
        """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
