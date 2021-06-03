#!/usr/bin/python3
"""Defines an JSON-file-to-Object funciton."""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file."""
    with open(filename) as json_f:
        return json.load(json_f)
