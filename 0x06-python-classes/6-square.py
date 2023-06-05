#!/usr/bin/python3
"""Class Square"""


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
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """size settere"""
        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple and len(value) != 2 and \
                not isinstance(value[0], int) and\
                not isinstance(value[1], int) and\
                value[0] < 0 and value[1] < 0:
            raise (TypeError("position must be a tuple of 2 positive integers"))
        else:
            self.__position = value

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.size):
            print(' ' * self.__position[0] + "#" * self.size)
