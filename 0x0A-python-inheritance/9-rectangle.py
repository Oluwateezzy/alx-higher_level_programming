#!/usr/bin/python3
"""base geo"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """strng rep"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """repr"""
        return f"Rectangle({self.__width}, {self.__height})"
