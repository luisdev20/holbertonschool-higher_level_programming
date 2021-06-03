#!/usr/bin/python3
"""Defines a string append-write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8)

    Return: The number of characters"""
    with open(filename, mode="a", encoding="utf-8") as my_file:
        my_file.write(text)
        added_chars = my_file.tell()
    return (added_chars)
