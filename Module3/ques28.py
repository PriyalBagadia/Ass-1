# Write a Python program to remove an empty tuple(s) from a list of tuples.

def remove_empty_tuples(list_of_tuples):
    return [tup for tup in list_of_tuples if tup]

# Example usage:
my_list = [(1, 2), (), (3, 4), (), (5, 6), ()]
cleaned_list = remove_empty_tuples(my_list)
print(cleaned_list)