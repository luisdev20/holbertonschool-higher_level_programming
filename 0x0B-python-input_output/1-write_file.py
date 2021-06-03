#!/usr/bin/python3
"""Defines a function that write a string to text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file UTF8

    Returns the number of characters written."""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
        chars = a_file.tell()
    return (chars)
