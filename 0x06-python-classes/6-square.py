#!/usr/bin/python3
"""
Class Square
- size, position private properties
- method of area and method of print_square
- getter and setters.
"""


class Square:
    """Class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        self.__size = size
        self.__position = position

    def area(self):
        """area of square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """size getter"""
        return (self.__size)

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if (type(value) is not tuple) or (len(value) != 2)\
                or (value[0] < 0) or (value[1] < 0)\
                type(value[0]) is not int\
                type(value[1]) is not int:
            raise (TypeError("position must be a tuple of 2 positive integer"))
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        """size settere"""
        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            for bl in range(self.__position):
                print()
            for rw in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
