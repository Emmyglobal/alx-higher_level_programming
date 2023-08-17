#!/usr/bin/python3
# A Function that adds all unique integers in a list
# (only once for each integer).

def uniq_add(my_list=[]):
    sum = 0
    for i in set(my_list):
        sum += i
    return(sum)
