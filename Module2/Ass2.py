# 1...Write a Python program to check if a number is positive, negative or
# zero.

# def check_number(num):
#     if num > 0:
#         print(f"{num} is positive.")
#     elif num < 0:
#         print(f"{num} is negative.")
#     else:
#         print("The number is zero.")

# while True:
#     num = float(input("Enter a number : "))
#     check_number(num)






# 2...Write a Python program to get the Factorial number of given number.

# number = int(input("Enter a number to calculate its factorial: "))

# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     factorial = 1
#     for i in range(1, number + 1):
#         factorial *= i
#     print("The factorial of", number, "is:", factorial)






# 3...Write a Python program to get the Fibonacci series of given range.
    
# def fibonacci_series(n):
#     fib_series = [0, 1]
#     while True:
#         next_fib = fib_series[-1] + fib_series[-2]
#         if next_fib > n:
#             break
#         fib_series.append(next_fib)
#     return fib_series

# range_limit = int(input("Enter the range limit to generate Fibonacci series: "))
# fib_series = fibonacci_series(range_limit)
# print("Fibonacci series within the range up to", range_limit, "is:")
# print(fib_series)






# 4...How memory is managed in Python?

# Python's memory management relies on reference counting, garbage collection, and memory pooling.
# Reference counting tracks the number of references to objects, garbage collection handles cyclic references 
# and unreachable objects, and memory pooling preallocates memory blocks to reduce allocation overhead. 
# This combination ensures efficient memory usage without requiring manual memory management by developers.






# 5...What is the purpose continue statement in python?

# the continue statement is used inside loops (such as for loops or while loops) to skip the rest of the current iteration
# and proceed to the next iteration of the loop.

# The purpose of the continue statement is to alter the flow of control within the loop without exiting the loop entirely.
# When the continue statement is encountered, the remaining code within the loop for the current iteration is skipped, 
# and the loop proceeds to the next iteration.






# 6...Write python program that swap two number with temp variable and without temp variable.

# Swap two numbers using a temporary variable

# def swap_with_temp(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b

# num1 = 5
# num2 = 10
# print("Before swapping:", num1, num2)    

# num1, num2 = swap_with_temp(num1, num2)
# print("After swapping:", num1, num2)


# Swap two numbers without using a temporary variable

# def swap_without_temp(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b

# # Test the function
# num1 = 5
# num2 = 10
# print("Before swapping:", num1, num2)

# num1, num2 = swap_without_temp(num1, num2)
# print("After swapping:", num1, num2)






# 7...Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")






# 8...Write a Python program to test whether a passed letter is a vowel or not.

# vowels = {'a', 'e', 'i', 'o', 'u'}

# input_letter = input("Enter a letter: ").lower()

# if len(input_letter) == 1 and input_letter.isalpha():
#     if input_letter in vowels:
#         print(f"{input_letter} is a vowel.")
#     else:
#         print(f"{input_letter} is not a vowel.")
# else:
#     print("Please enter a single letter.")






# 9... Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
    
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# num3 = int(input("Enter the third integer: "))

# if num1 == num2 or num2 == num3 or num3 == num1:
#     result = 0
# else:
#     result = num1 + num2 + num3

# print("The sum of three integers is:", result)






# 10...Write a Python program that will return true if the two given integervalues are equal or their sum or difference is 5.

# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))

# # Check if the conditions are satisfied
# result = num1 == num2 or abs(num1 - num2) == 5 or num1 + num2 == 5

# print("Result:", result)






# 11...Write a python program to sum of the first n positive integers.

# n = int(input("Enter the value of n: "))

# # Calculate the sum of the first n positive integers using the formula
# result = n * (n + 1) // 2

# print("The sum of the first", n, "positive integers is:", result)






# 12...Write a Python program to calculate the length of a string.

# string = input("Enter a string: ")
# print("Length of the string is:", len(string))






# 13...Write a Python program to count the number of characters (character frequency) in a string

# from collections import Counter

# input_string = input("Enter a string: ")

# # Counting character frequencies
# result = Counter(input_string)

# print("Character frequencies:")
# for char, frequency in result.items():
#     print(f"'{char}': {frequency}")






# 14...What are negative indexes and why are they used?

# Negative indexes in Python are used to access elements from the end of a sequence. 
# They start from -1 for the last element and count backward. 
# They provide a convenient way to access elements relative to the end of the sequence without needing to know its length.






# 15...Write a Python program to count occurrences of a substring in a string.

# string = "hello, hello, hello, how low?"
# substring = "hello"
# print("Occurrences of '{}' in '{}': {}".format(substring, string, string.count(substring)))






# 16...Write a Python program to count the occurrences of each word in a given sentence

# from collections import Counter

# sentence = "Hello,My name is Priyal!"
# word_occurrences = Counter(sentence.split())
# for word, count in word_occurrences.items():
#     print(f"'{word}': {count}")






# 17...Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

# def swap_and_combine(str1, str2):
#     return str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]

# string1 = "Hey"
# string2 = "Priyal"
# print("Result:", swap_and_combine(string1, string2))






# 18... Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.

# def add_ing_ly(string):
#     if string.endswith('ing'):
#         return string + 'ly'
#     return string + 'ing'

# strings = ["play", "playing", "hi", "go"]
# for string in strings:                   
#     print(f"Original: {string}, Result: {add_ing_ly(string)}")






# 19...Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.

# def replace_not_poor(string):
#     index_not = string.find('not')
#     index_poor = string.find('poor')

#     if index_not != -1 and index_poor != -1 and index_not < index_poor:
#         return string[:index_not] + 'good' + string[index_poor + 4:]
#     return string

# input_string = "The weather is not poor today."
# result_string = replace_not_poor(input_string)
# print("Result:", result_string)






# 20...Write a Python function that takes a list of words and returns the length of the longest one.

# def longest_word_length(words):
#     longest_word = max(words, key=len, default="")
#     return len(longest_word), longest_word

# words_list = ["apple", "banana", "orange", "strawberry", "pineapple"]
# length, word = longest_word_length(words_list)
# print("Length of the longest word:", length,",",word)






# 21...Write a Python function to reverses a string if its length is a multiple of 4.
 
# def reverse_string_if_multiple_of_four(string):
#     return string[::-1] if len(string) % 4 == 0 else string

# # Continuous input and output
# while True:
#     input_string = input("Enter a string (type 'exit' to quit): ")
#     if input_string.lower() == "exit":
#         break
#     print("Output:", reverse_string_if_multiple_of_four(input_string))





#23...Write a Python function to insert a string in the middle of a string.

# def insert_string_in_middle(original_string, string_to_insert):
#     return original_string[:len(original_string)//2] + string_to_insert + original_string[len(original_string)//2:]

# original_string = "Hello, world!"
# string_to_insert = "Python"
# result = insert_string_in_middle(original_string, string_to_insert)
# print("Output:", result)  






# 22...Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

a="priyal"
b=a[:2]+a[-2:]
print("ourput : ",b)
