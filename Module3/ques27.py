# Write a Python program to find the repeated items of a tuple.

def find_repeated_items(tup):
    repeated_items = []
    for item in tup:
        if tup.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

# Example usage:
my_tuple = (1, 2, 2, 3, 4, 4, 5, 5)
repeated = find_repeated_items(my_tuple)
print(repeated)