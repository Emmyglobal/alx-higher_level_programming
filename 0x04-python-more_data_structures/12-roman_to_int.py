#!/usr/bin/python3
from functools import reduce
def roman_to_int(roman_string):
    letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    listOfNum = []
    sumTheList = 0
    for i in roman_string:
            for k, v in letters.items():
                if i == k:
                     listOfNum.append(v)
    for i in range(len(listOfNum) - 1):
        if listOfNum[i] < listOfNum[i + 1]:
            sumTheList -= listOfNum[i]
        else:
            sumTheList += listOfNum[i]
    sumTheList += listOfNum[-1]
    return sumTheList
