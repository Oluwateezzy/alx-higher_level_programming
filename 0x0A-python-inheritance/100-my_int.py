#!/usr/bin/python3
"""int"""


class MyInt(int):
    """My int"""
    def __eq__(self, other):
        """eq"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """ne"""
        return not super().__ne__(other)
