#!/usr/bin/python3
import random
number = random.randint(-10, 10)
i = 1
while (i == number):
    i += 1
if number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is not here")
