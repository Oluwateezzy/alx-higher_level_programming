#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictonary is None:
        return None
    max = a_dictionary.values()[0]
    for a in a_dictionary.keys():
        if a_dictionary[a] > max:
            max = a_dictionary[a]
    return max
