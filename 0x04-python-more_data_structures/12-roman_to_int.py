#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roma = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and \
                roma[roman_string[i]] < roma[roman_string[i + 1]]:
            total = total - roma[roman_string[i]]
        else:
            total = total + roma[roman_string[i]]
    return total
