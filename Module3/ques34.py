# Write a Python script to check if a given key already exists in a dictionary.

def key_exists_in_dict(key, d):
    return key in d

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}

print("Does 'a' exist in the dictionary?", key_exists_in_dict('a', my_dict))
print("Does 'z' exist in the dictionary?", key_exists_in_dict('z', my_dict))