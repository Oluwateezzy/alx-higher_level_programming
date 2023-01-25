#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        lis = ord(i)
        if lis >= 97 and lis <= 122:
            result += chr(lis - 32)
        else:
            result += chr(lis)
    print("{}".format(result))
