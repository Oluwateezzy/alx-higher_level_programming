#!/usr/bin/python3
lis = ['e', 'q']
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in lis:
        print("{}".format(chr(i)), end="")
