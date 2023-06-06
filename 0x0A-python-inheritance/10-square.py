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
s = Square(13)

print(s)
print(s.area())
