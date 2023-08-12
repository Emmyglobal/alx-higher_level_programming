#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    sum1 = 0
    i = 1
    if (length == 0):
        print("{}".format(sum1))
    else:
        while i <= length:
            sum1 += int(argv[i])
            i += 1
        print("{}".format(sum1))
