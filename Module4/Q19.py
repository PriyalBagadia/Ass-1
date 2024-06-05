# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

# -> In Python, you can handle exceptions using the try, except, and finally blocks. 
# Here's how you can handle exceptions with try, except, and finally:

# try Block: The try block is used to enclose the code that might raise an exception.

# except Block: The except block is used to handle specific exceptions that occur within the try block. 
# You can have multiple except blocks to handle different types of exceptions.

# finally Block: The finally block is executed regardless of whether an exception occurs or not. 
# It's typically used for cleanup tasks that must be performed, such as closing files or releasing resources.

# Example 1: Handling Specific Exceptions
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("End of program.")

# Example 2: Handling Any Exception
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except Exception as e:
    print("An error occurred:", e)
finally:
    print("End of program.")

# Example 3: Using else Block
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No exceptions occurred.")
finally:
    print("End of program.")
