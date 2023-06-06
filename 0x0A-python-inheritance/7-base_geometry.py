#!/usr/bin/python3
"""base geo"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """integer validation"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
