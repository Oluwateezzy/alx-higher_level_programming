#!/usr/bin/python3
"""load save and add"""
import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("load_from_json_file").load_from_json_file

try:
    load = load_from_json_file("add_item.json")
except FileNotFoundError:
    load = []

argc = len(sys.argv)
for i in range(1, argc):
    load.append(sys.argv[i])
save_to_json_file(load)
