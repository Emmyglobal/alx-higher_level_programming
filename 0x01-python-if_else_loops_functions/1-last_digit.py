#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = 1
while (i == number):
    i += 1
# 1. Get the string representation
number = repr(number)
# 2. Access the last string of the digit string:
last = number[-1]
# 3. Convert the last digit string to an integer:
last = int(last)
if (last > 5):
    print(f"Last digit of {number} is {last} and is greater than 5")
elif (last == 0):
    print(f"Last digit of {number} is {last} and is 0")
elif (last < 6 and last != 0):
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
