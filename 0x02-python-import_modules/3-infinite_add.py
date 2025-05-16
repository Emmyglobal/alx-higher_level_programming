#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv
    count = len(sys.argv)
    sums = 0
    for i in range(1, count):
       sums += int(arg[i])
    print(sums)

