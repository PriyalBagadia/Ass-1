# Write a Python program to reverse a tuple.

def reverse_tuple(tup):
    return tuple(reversed(tup))

# Example usage:
my_tuple = (5, 4, 3, 2, 1)
reversed_tuple = reverse_tuple(my_tuple)
print(reversed_tuple)