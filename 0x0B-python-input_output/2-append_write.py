#!/usr/bin/python3
"""Defines a string append-write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8)

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file filename.
    Return:
        The number of characters.
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
