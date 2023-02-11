#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        number_of_instances += 1

    def __str__(self):
        """object representation"""
        res = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            if i == self.__height - 1:
                res += "#" * self.__width
            else:
                res += "#" * self.__width + "\n"
        return res

    def __repr__(self):
        """object represenattion"""
        return f'Rectangle({str(self.__width)}, {str(self.__height)})'

    def __del__(self):
        number_of _instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of a Rectangle"""
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter
