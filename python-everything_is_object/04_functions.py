#!/usr/bin/python3
def greet():
    print("Hello!")


greet()


def greet_name(name):
    print(f"Hello, {name}!")


greet_name("Alice")


def add(a, b):
    return a + b


result = add(5, 3)
print(result)


def multiply(x, y):
    return x * y


product = multiply(4, 7)
print(product)


def get_info(name, age):
    return f"{name} is {age} years old"


info = get_info("Bob", 30)
print(info)


def greet_with_default(name="Guest"):
    print(f"Welcome, {name}!")


greet_with_default()
greet_with_default("John")


def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return a / b


print(calculate(10, 5))
print(calculate(10, 5, "subtract"))
print(calculate(10, 5, "multiply"))
