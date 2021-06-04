#!/usr/bin/python3
"""Define Square a class that inherits from Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size):
        """Instantation of Square.
        Args:
            size(int): must be private, positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
