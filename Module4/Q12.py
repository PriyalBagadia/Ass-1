# Write a Python program to copy the contents of a file to another file.

def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        content = source.read()
    
    with open(destination_file, 'w') as destination:
        destination.write(content)

source_file = 'source.txt'

destination_file = 'destination.txt'

copy_file(source_file, destination_file)

print(f'Contents of {source_file} have been copied to {destination_file}')
