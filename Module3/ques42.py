# Write a Python program to print all unique values in a dictionary.

def unique_values(dictionary):
    unique_vals = set()
    for value_list in dictionary.values():
        unique_vals.update(value_list)
    return unique_vals

# Sample data
sample_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}

# Print unique values
print(unique_values(sample_dict))
