#!/usr/bin/python3
"""Defines MyList class that inherits from list"""


class MyList(list):
    """Represents a list subclass from list class"""

    def print_sorted(self):
        """Prints a list, sorted (ascending)"""
        print(sorted(self))
