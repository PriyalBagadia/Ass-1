# Write a Python program to find the highest 3 values in a dictionary

def highest_3_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_items[:3])

# Sample data
sample_dict = {'a': 100, 'b': 300, 'c': 200, 'd': 500, 'e': 400}

# Find highest 3 values
print(highest_3_values(sample_dict))
