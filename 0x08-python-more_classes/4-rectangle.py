#!/usr/bin/python3
"""Represent a rectangle."""


class Rectangle:
    """Defines a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (self.width * 2 + self.height * 2)

    def __str__(self):
        """Return the friendly-printable representation of the rectangle.

        A representation of the rectangle with the # char.
        """
        if self.width == 0 or self.height == 0:
            return ("")

        rectang = []
        for i in range(self.height):
            for j in range(self.width):
                rectang.append('#')
            rectang.append("\n")
        return ("".join(rectang))

    def __repr__(self):
        """Return the formal representation of the printable rectangle."""
        coord = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (coord)
