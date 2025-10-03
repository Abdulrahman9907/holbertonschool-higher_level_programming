age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1

for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

number = 15
if number > 10:
    if number < 20:
        print("Number is between 10 and 20")
