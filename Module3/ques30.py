# Write a Python program to convert a list of tuples into a dictionary.

def list_of_tuples_to_dict(list_of_tuples):
    return dict(list_of_tuples)

# Example usage:
my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
my_dict = list_of_tuples_to_dict(my_list)
print(my_dict)