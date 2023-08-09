#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
    la = number % 10
else:
    number = number * (-1)
    la = number % 10
    number = number * (-1)
    la = la * (-1)
if la > 5:
    print(f"Last digit of {number:d} is {la:d} and is greater than 5")
elif la == 0:
    print(f"Last digit of {number:d} is {la:d} and is 0")
else:
    print(f"Last digit of {number:d} is {la:d} and is less than 6 and not 0")
