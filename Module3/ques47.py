
# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string: 'w3resource'
# Expected output:
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

def create_char_count_dict(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Sample string
sample_string = 'w3resource'

# Create dictionary
result_dict = create_char_count_dict(sample_string)

# Print result
print(result_dict)
