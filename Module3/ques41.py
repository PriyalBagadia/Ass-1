# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

from collections import Counter

def combine_dictionaries(d1, d2):
    # Create Counters from the dictionaries
    counter1 = Counter(d1)
    counter2 = Counter(d2)
    
    # Add Counters together
    result = counter1 + counter2
    
    return result

# Given dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries
combined_dict = combine_dictionaries(d1, d2)

# Print the result
print(combined_dict)
