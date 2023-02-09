#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Constructor"""
        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """area of square"""
        return (self.__size ** 2)
    def size(self):
        return self.__size
    def size(self, size):
       self.__size = size
