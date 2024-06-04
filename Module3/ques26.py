# Write a Python program to replace last value of tuples in a list.

def replace_last_value(tuples_list, new_value):
    return [t[:-1] + (new_value,) for t in tuples_list]

# Example usage:
my_list = [(1, 2), (3, 4), (5, 6)]
new_list = replace_last_value(my_list, 10)
print(new_list)