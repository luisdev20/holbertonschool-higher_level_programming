#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Return a list of available attributte and methods of the object"""
    return (dir(obj))
