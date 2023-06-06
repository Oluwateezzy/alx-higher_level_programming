#!/usr/bin/python3
"""Mylist"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
