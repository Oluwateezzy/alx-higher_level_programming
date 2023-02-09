#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def size(self, value):
        """Constructor"""
        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    def area(self):
        """area of square"""
        return (self.__size ** 2)
    def size(self):
        return self.__size
