#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    arg = sys.argv
    count = len(arg)
    if count != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = arg[2]
        no1 = int(arg[1])
        no2 = int(arg[3])
        if op == "+":
            print(f"{no1} {op} {no2} = {add(no1, no2)}")
            exit(0)
        elif op == "-":
            print(f"{no1} {op} {no2} = {sub(no1, no2)}")
            exit(0)
        elif op == "*":
            print(f"{no1} {op} {no2} = {mul(no1, no2)}")
            exit(0)
        elif op == "/":
            print(f"{no1} {op} {no2} = {div(no1, no2)}")
            exit(0)
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
