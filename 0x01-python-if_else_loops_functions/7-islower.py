#!/usr/bin/python3
def islower(c):
    asciCode = ord(c)
    for i in range(97, 123):
        if i == asciCode:
            return True
    else:
        return False
