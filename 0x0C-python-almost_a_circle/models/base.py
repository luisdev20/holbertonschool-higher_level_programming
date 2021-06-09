#!/usr/bin/python3
"""Defines a Base Class."""
import json


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
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [objs.to_dictionary() for objs in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
