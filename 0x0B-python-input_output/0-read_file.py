#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""

    with open(filename, 'utf8') as file:
        print(file.read(), end="")
