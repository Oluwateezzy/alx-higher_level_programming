#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """inherit"""
    return False if type(obj) == a_class else isinstance(obj, a_class)
