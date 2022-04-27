#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = number % -10
if lastdigit > 5:
    value = 'and is greater than 5'
elif lastdigit == 0:
    value = 'and is 0'
else:
    value = 'and is less than 6 and not 0'
print('Last digit of', number, 'is', lastdigit, value)
