#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        if position[0] < 0 || position[1] < 0:
            raise (TypeError("position must be a tuple of 2 positive integers"))
        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """area of square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if value[0] < 0 | value[1] < 0:
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
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
