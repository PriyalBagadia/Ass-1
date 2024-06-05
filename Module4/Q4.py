# Write a Python program to read first n lines of a file.

def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line, end='')

file_path = 'example.txt'
n = 3

read_first_n_lines(file_path, n)
