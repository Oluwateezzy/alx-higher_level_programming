#!/usr/bin/python3
"""create object from a json file"""
import json


def load_from_json_file(filename):
    """create object from a json file"""

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
