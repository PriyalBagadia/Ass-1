# Write a Python function that checks whether a passed string is palindrome or not
def is_palindrome(string):
    return string == string[::-1]

# Test the function
test_string = "radar"
if is_palindrome(test_string):
    print(test_string, "is a palindrome.")
else:
    print(test_string, "is not a palindrome.")
