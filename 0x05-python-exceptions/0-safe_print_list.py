#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    cont = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            cont += 1
        except:
            pass
        i += 1
    print()
    return cont
