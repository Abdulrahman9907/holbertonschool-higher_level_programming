#!/usr/bin/python3
# filepath: /Users/abdulrahmanalhussainy/Documents/Website/2-print.py
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
