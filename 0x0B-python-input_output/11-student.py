#!/usr/bin/python3
"""Defines a student by class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student."""
        if (type(attrs) == list and
                all(type(each) == str for each in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for k, v in json.items():
            setattr(self, k, v)
