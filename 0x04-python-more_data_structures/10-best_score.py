#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = sorted(list(a_dictionary.values()))
    return (max[-1])
