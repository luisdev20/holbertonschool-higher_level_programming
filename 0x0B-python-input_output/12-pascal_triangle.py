#!/usr/bin/python3s
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers

    Represents the Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        subtri = triangle[-1]
        tmp = [1]
        for i in range(len(subtri) - 1):
            tmp.append(subtri[i] + subtri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
