# Write a Python program to check multiple keys exists in a dictionary

def check_multiple_keys_exist(keys, d):
    return all(key in d for key in keys)

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b', 'z']

if check_multiple_keys_exist(keys_to_check, my_dict):
    print("All keys exist in the dictionary.")
else:
    print("At least one key does not exist in the dictionary.")