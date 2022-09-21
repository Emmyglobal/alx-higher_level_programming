#!/usr/bin/python3
def uppercase(str):
    check = ord(str)
    for i in str:
        if(check >= 97) and (check <= 122):
            print("{}".format(str))
