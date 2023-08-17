#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    arg = sys.argv
    num_arg = len(arg) - 1
    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif arg[2] == '+':
        add = calculator_1.add(int(arg[1]), int(arg[3]))
        print("{} + {} = {}".format(arg[1], arg[3], add))
    elif arg[2] == '-':
        sub = calculator_1.sub(int(arg[1]), int(arg[3]))
        print("{} - {} = {}".format(arg[1], arg[3], sub))
    elif arg[2] == '*':
        mul = calculator_1.mul(int(arg[1]), int(arg[3]))
        print("{} * {} = {}".format(arg[1], arg[3], mul))
    elif arg[2] == '/':
        div = calculator_1.div(int(arg[1]), int(arg[3]))
        print("{} / {} = {}".format(arg[1], arg[3], div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
