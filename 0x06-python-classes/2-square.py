#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Constructor"""
        try:
            self.__size = self
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
