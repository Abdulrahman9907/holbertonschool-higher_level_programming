#!/usr/bin/python3
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])
print(numbers[-1])

numbers.append(6)
print(numbers)

numbers.remove(3)
print(numbers)

print(len(numbers))

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

coordinates = (10, 20)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

point = (5, 10, 15)
x, y, z = point
print(x)
print(y)
print(z)

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)
print(person["name"])
print(person["age"])

person["email"] = "alice@example.com"
print(person)

del person["city"]
print(person)

for key in person:
    print(f"{key}: {person[key]}")

unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

unique_numbers.add(6)
print(unique_numbers)

unique_numbers.add(3)
print(unique_numbers)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
print(matrix[1][2])
