#!/usr/bin/python3
# filepath: /Users/abdulrahmanalhussainy/Documents/Website/2-print.py
for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
