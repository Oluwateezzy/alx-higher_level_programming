#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dicty = a_dictionary
    for i in dicty.keys():
        if dicty[i] == value:
            del a_dictionary[i]
    return a_dictionary
