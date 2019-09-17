#!/usr/bin/python3
def no_c(my_string):
        str1 = ""
        for i in my_string:
            if i is not 'c' and i is not 'C':
                str1 += i
        return str1
