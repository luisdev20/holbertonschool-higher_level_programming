#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys """
    [print("{}: {}".format(s, a_dictionary[s])) for s in sorted(a_dictionary)]
