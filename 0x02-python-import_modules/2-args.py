#!/usr/bin/python3
import sys
if __name__ == "__main__":
    leng = len(sys.argv)
    if leng >= 2:
        if leng == 2:
            arg = "argument"
        else:
            arg = "arguments"
        print("{} {}:".format(leng - 1, arg))
        for i in range(1, leng):
                cont = i
                print("{}: {}".format(cont, sys.argv[i]))
    else:
        print("0 arguments.")
