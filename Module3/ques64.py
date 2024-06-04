# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(decimal_numbers):
    maximum = max(decimal_numbers)
    minimum = min(decimal_numbers)
    return maximum, minimum

# Test the function
decimal_numbers = [3.14, 2.71, 1.618, 0.577, 2.718]
maximum, minimum = find_max_min(decimal_numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)
