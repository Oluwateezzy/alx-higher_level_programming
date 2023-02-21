#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    text
    indentation
    raises
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    str1 = ""
    strD = []
    for i in text:
        if i in ".:?":
            str1 += i
            strD.append(str1)
            str1 = ""
        else:
            str1 += i
    strD.append(str1)
    for i in range(len(strD)):
        if i == len(strD) - 1:
            print(strD[i].strip(), end="")
        else:
            print(strD[i].strip())
            print()
