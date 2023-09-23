#!/usr/bin/python3
"""Square representation"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square representation inheriting from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instance initiialization of Square

        Args:
            size(int): size of square
            x(int): x coordinate
            y(int): y coordinate
            id(int): generic identifier for the square
        """
        # Call the super class with id, x, y, width and height
        # this super call will use the logic of the
        # __init__ of the Rectangle class
        # The width and height must be assigned to the value of size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter function for the size of the square.
        Returns: the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating instance attributes using postional args
            and keyword arguments
        """
        if len(args) != 0:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.size = args[1]
            except IndexError:
                pass
            try:
                self.x = args[2]
            except IndexError:
                pass
            try:
                self.y = args[3]
            except IndexError:
                pass

        else:
            try:
                self.id = kwargs["id"]
            except KeyError:
                pass
            try:
                self.size = kwargs["size"]
            except KeyError:
                pass
            try:
                self.x = kwargs["x"]
            except KeyError:
                pass
            try:
                self.y = kwargs["y"]
            except KeyError:
                pass

    def __str__(self):
        """Method overridden to return desired string
        for class Square

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        shape = f"[{type(self).__name__}] ({self.id})"
        coords = f"{self.x}/{self.y}"
        sides = f"{self.width}"
        return f"{shape} {coords} - {sides}"

    def to_dictionary(self):
        """Returns a dictionary representation of a Square."""
        return_dict = {}
        return_dict['id'] = self.id
        return_dict['size'] = self.size
        return_dict['x'] = self.x
        return_dict['y'] = self.y
        return return_dict
