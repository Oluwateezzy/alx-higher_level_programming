#!/usr/bin/python3

"""Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return self.__size ** 2

    def __str__(self):
        """string representation"""
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """repr"""
        return f"Square({self.__size})"
