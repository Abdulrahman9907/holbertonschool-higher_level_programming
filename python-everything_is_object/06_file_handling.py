file = open("sample_data.txt", "r")
content = file.read()
print(content)
file.close()

with open("sample_data.txt", "r") as file:
    content = file.read()
    print(content)

with open("sample_data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")

with open("output.txt", "a") as file:
    file.write("Appending a new line.\n")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)

data = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("lines.txt", "w") as file:
    file.writelines(data)

with open("lines.txt", "r") as file:
    for line in file:
        print(line.strip())
