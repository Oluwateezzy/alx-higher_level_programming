#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """append to a file"""

    with open(filename, mode='a', encoding="utf-8") as file:
        file.write(text)
        return (len(text))
