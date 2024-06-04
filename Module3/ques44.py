# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd

from itertools import product

def letter_combinations(dictionary):
    keys = dictionary.keys()
    values = dictionary.values()
    combinations = product(*values)
    result = [''.join(comb) for comb in combinations]
    return result

# Sample data
sample_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

# Display all combinations
print(letter_combinations(sample_dict))
