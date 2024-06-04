# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

def create_dict_with_range(start, end):
    return {i: None for i in range(start, end + 1)}

# Example usage:
my_dict = create_dict_with_range(1, 15)
print(my_dict)