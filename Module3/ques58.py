# Write a Python program to read a random line from a file.

import random

def read_random_line(filename):
    with open(filename, 'r') as file:
        # Count the total number of lines in the file
        total_lines = sum(1 for line in file)
        
        # Generate a random line number
        random_line_number = random.randint(1, total_lines)
        
        # Seek to the random line
        file.seek(0)  # Reset file pointer to the beginning
        for _ in range(random_line_number - 1):
            file.readline()
        
        # Read the random line
        random_line = file.readline().strip()
        
        return random_line

# Test the function
filename = 'sample_file.txt'  # Replace 'sample_file.txt' with the path to your file
random_line = read_random_line(filename)
print("Random line from the file:", random_line)
