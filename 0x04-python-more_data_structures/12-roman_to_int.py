#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rom_nu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    cont = 0
    for i in roman_string:
        if i in rom_nu:
            value = rom_nu[i]
        else:
            value = 0
        if num is 0:
            num += value
            cont += 1
            continue
        if i == 'V' or i == 'X':
            if roman_string[cont - 1] == 'I':
                value -= 2
        elif i == 'L' or i == 'C':
            if roman_string[cont - 1] == 'X':
                value -= 20
        elif i == 'D' or i == 'M':
            if roman_string[cont - 1] == 'C':
                value -= 200
        num += value
        cont += 1
    return num
