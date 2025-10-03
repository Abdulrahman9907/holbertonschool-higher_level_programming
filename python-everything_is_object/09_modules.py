import math

print(math.pi)
print(math.sqrt(16))
print(math.ceil(4.3))
print(math.floor(4.7))

from math import sqrt, pow

print(sqrt(25))
print(pow(2, 3))

import random

print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.random())

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

today = datetime.date.today()
print(today)

from datetime import timedelta

future = today + timedelta(days=7)
print(future)

import os

print(os.getcwd())

import sys

print(sys.version)
print(sys.platform)
