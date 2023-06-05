#!/usr/bin/python3
"""mmagic class"""

import math


class MagicClass:
    """magic class"""
    def __init__(self, radius):
        """constructor"""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area"""
        return 2 ** self.__radius * math.pi

    def circumference(self):
        """Circumference"""
        return 2 * math.pi * self.__radius
