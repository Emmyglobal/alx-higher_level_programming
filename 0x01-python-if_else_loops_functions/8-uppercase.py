#!/usr/bin/python3
def uppercase(str):
    check = ord(str)
    for i in str:
        if(check >= 65) and (check <= 90):
            print("{}".format(str))
