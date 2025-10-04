#!/usr/bin/python3
try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    number = int("abc")
except ValueError:
    print("Invalid conversion")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range")

try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Operation successful")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Operation successful")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always executes")

# Example with raising custom exceptions
# (commented to avoid blocking automation)
# try:
#     age = int(input("Enter age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative")
# except ValueError as e:
#     print(f"Error: {e}")

try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(f"Error: {e}")

try:
    x = 10 / 0
except (ZeroDivisionError, ValueError, TypeError):
    print("An error occurred")
