# Write a Python program to write a list to a file.

def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

file_path = 'output.txt'

data_to_write = ['Hello', 'World', 123, 3.14, True]

write_list_to_file(file_path, data_to_write)

print(f'List has been written to {file_path}')
