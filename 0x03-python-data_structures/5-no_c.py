#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for i in my_string:
        if i in "cC":
            pass
        else:
            copy = copy + i
    return copy
