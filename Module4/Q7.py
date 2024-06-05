# Write a Python program to read a file line by line store it into a variable.

def read_file_to_variable(file_path):
    file_content = ""
    
    with open(file_path, 'r') as file:
        for line in file:
            file_content += line
    
    return file_content

file_path = 'example.txt'

content = read_file_to_variable(file_path)

print(content)
