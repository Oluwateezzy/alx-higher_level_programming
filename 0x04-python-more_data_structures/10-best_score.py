#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None | len(a_dictionary) == 0:
        return None
    max = 0
    str = ""
    for a in a_dictionary.keys():
        if a_dictionary[a] > max:
            max = a_dictionary[a]
            str = a
    return (str)
