# Write a Python function to check whether a number is perfect or not.
def is_perfect_number(num):
    divisor_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisor_sum == num

# Test the function
number = 28
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
