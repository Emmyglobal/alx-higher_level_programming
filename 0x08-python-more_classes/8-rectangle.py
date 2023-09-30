#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Class representation of a rectangle.
    Attributes:
        number_of_instances (int): The number of rectangle instances created.
        print_symbol (any): Custom symbol used as string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): instance width. Defaults to 0.
            height (int): instance height. Defaults to 0.
        """
        # increase the number of instances at instantiation
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function for the width of the rectangle.
        Returns: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for the height of the rectangle.

        Args:
            value: The newly given height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the string representation of the Rectangle.

        Represents the rectangle with the `print_symbol` character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        reps = []
        for i in range(self.__height):
            [reps.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                reps.append("\n")
        return ("".join(reps))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion instance of a Rectangle."""
        # decrease the number of instances at deletion
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
