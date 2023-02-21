#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """write to file"""

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
