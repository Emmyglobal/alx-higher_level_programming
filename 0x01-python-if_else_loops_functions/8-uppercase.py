#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        check = ord(str[i])
        if 97 <= check <= 122:
            check = check - 32
        print("{:c}".format(check), end=""))
    print()
