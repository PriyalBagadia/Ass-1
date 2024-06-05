# Write a Python program to count the number of lines in a text file.

def count_lines_in_file(file_path):
    line_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
    
    return line_count

file_path = 'example.txt'

number_of_lines = count_lines_in_file(file_path)

print(f'The number of lines in the file is: {number_of_lines}')
