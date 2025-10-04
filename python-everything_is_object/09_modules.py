#!/usr/bin/python3
import math
from math import sqrt, pow
import random
import datetime
from datetime import timedelta
import os
import sys

print(math.pi)
print(math.sqrt(16))
print(math.ceil(4.3))
print(math.floor(4.7))

print(sqrt(25))
print(pow(2, 3))

print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.random())

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

today = datetime.date.today()
print(today)

future = today + timedelta(days=7)
print(future)

print(os.getcwd())

print(sys.version)
print(sys.platform)
