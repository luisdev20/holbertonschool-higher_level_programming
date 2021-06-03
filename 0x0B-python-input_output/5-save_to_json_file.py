#!/usr/bin/python3
"""Defines a object-to-json-file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to text, using a JSON representation.

    Args:
        my_obj (obj): object to represent by json file.
        filename (str): The name of the file.
    Returns:
        Nothing.
    """
    with open(filename, mode='w') as json_f:
        json.dump(my_obj, json_f)
