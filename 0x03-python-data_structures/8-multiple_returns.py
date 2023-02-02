#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        ch = None
    else:
        ch = sentence[0]

    return (length, ch)
