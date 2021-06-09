#!/usr/bin/python3
"""Defines a Base Class."""


class Base:
    """
    The base class of all the other classes.

    In order to manage an id attribute in all classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantation with none id.

        Args:
            id (int): The id of new classes in ptoject.
        """
        self.id = id
        if id == None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
