# Write a Python function to check whether a number is in a given range
def in_range(number, start, end):
    return start <= number <= end

# Test the function
num = 5
start_range = 1
end_range = 10

if in_range(num, start_range, end_range):
    print(num, "is in the range from", start_range, "to", end_range)
else:
    print(num, "is not in the range from", start_range, "to", end_range)
