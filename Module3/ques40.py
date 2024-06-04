# Write a Python program to map two lists into a dictionary

def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example usage:
keys = ['a', 'b', 'c']
values = [1, 2, 3]

result_dict = lists_to_dict(keys, values)
print(result_dict)