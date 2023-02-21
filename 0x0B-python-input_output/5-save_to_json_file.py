#!/usr/bin/python3
"""save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, mode='w') as file:
        file.write(json.dumps(my_obj))
