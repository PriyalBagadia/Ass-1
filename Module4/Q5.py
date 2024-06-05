# Write a Python program to read last n lines of a file.

from collections import deque

def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        last_n_lines = deque(file, maxlen=n)
    
    for line in last_n_lines:
        print(line, end='')

file_path = 'example.txt'
n = 3

read_last_n_lines(file_path, n)
