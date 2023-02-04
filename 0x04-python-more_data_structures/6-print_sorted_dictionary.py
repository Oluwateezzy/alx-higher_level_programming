#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in a_dictionary.keys().sort():
        print("{}: {}".format(i, a_dictionary[i]))
