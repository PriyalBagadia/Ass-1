# Write a Python script to concatenate following dictionaries to create a new one.

def concatenate_dicts(*dicts):
    concatenated_dict = {}
    for d in dicts:
        concatenated_dict.update(d)
    return concatenated_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

concatenated_dict = concatenate_dicts(dict1, dict2, dict3)
print(concatenated_dict)