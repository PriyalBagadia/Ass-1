# Write a Python program to read an entire text file.

file_path = 'example.txt'

with open(file_path, 'r') as file:
    content = file.read()

print(content)
