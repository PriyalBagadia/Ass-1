# Write a Python program to convert a tuple to a string.

def tuple_to_string(input_tuple):
    # Convert tuple to string by joining each element with a space
    result_string = ' '.join(map(str, input_tuple))
    return result_string

# Example usage
example_tuple = ('Hello', 'world', 'this', 'is', 'a', 'tuple')
result = tuple_to_string(example_tuple)
print(result)
