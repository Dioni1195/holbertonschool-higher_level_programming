#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum_weig = 0
    tot = 0
    for calf in my_list:
        sum_weig += calf[0] * calf[1]
        tot += calf[1]
    return sum_weig / tot
