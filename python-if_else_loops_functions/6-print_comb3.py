#!/usr/bin/python3
# filepath: /Users/abdulrahmanalhussainy/Documents/Website/2-print.py
for i in range(10):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=", " if not (i == 8 and j == 9)
              else "\n")
