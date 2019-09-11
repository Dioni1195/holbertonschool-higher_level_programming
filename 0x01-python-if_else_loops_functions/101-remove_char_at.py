#!/usr/bin/python3
def remove_char_at(str2, n):
    str1 = str2
    for i in range(0, len(str1)):
        if i == n:
            str1[i] = ""
    return str1
