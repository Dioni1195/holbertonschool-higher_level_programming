#!/usr/bin/python3
for i in range(122, 96,-1):
    if i % 2 != 0:
        check_value = 32
    else:
        check_value = 0
    print("{:c}".format(i - check_value), end="")
