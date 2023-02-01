#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    if len(argv) == 1:
        print(0)
    else:
        for i in range(1, len(argv)):
            total = total + int(argv[i])
        print(total)
