# Write a Python program to append text to a file and display the text.

file_path = 'example.txt'

text_to_append = 'This is the appended text.\n'

with open(file_path, 'a') as file:
    file.write(text_to_append)

with open(file_path, 'r') as file:
    content = file.read()

print(content)
