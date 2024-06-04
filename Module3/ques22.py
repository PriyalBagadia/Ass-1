# Write a Python program to check whether an element exists within a tuple.

def element_exists_in_tuple(input_tuple, element):
    # Check if the element exists in the tuple
    return element in input_tuple

# Example usage
example_tuple = (1, 2, 3, 4, 5)
element_to_check = 7

if element_exists_in_tuple(example_tuple, element_to_check):
    print(f"Element {element_to_check} exists in the tuple.")
else:
    print(f"Element {element_to_check} does not exist in the tuple.")
