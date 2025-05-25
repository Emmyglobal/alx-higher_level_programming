#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    multiplyAndSum = 0
    denominator = 0
    for i in my_list:
        x, y = i
        multiplyAndSum += (x * y)
        denominator += y
    res = multiplyAndSum / denominator
    return res   
