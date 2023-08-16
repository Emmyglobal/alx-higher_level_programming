#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num_par = len(sys.argv) - 1
    sum = 0
    for i in range(num_par):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
