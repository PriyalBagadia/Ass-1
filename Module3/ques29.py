# Write a Python program to unzip a list of tuples into individual lists.

def unzip_list_of_tuples(list_of_tuples):
    return list(zip(*list_of_tuples))

# Example usage:
my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
unzipped = unzip_list_of_tuples(my_list)
print(unzipped)