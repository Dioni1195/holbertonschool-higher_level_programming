#!/usr/bin/env python3
def uppercase(str):
    for i in range(len(str)):
        check_lower = ord(str[i])
        if check_lower >= 97 and check_lower < 123:
            check_lower -= 32
        if i != len(str) - 1:
            print("{}".format(chr(check_lower)), end="")
        else:
            print("{}".format(chr(check_lower)))
