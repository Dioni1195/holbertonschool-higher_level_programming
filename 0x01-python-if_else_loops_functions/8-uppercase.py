#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        check_lower = ord(str[i])
        if check_lower >= 97 and check_lower <= 122:
            check_lower -= 32
        print("{}".format(chr(check_lower)), end="")
    print()
