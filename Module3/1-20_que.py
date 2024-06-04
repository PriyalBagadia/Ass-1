# 1..What is List? How will you reverse a list?
# a list is a data structure that can hold an ordered collection of items.
# Lists are mutable, which means their elements can be changed after they are created.
# Lists can contain elements of different data types,
# and they are defined using square brackets [].

# num = [1, 2, 3, 4, 5]
# num.reverse()
# print(num) 




# 2..How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

# list1 = [2, 33, 222, 14, 25]
# list1 = list1[:-1]
# print(list1) 




# 3..Differentiate between append () and extend () methods? 
# -> append() method: append() method is used to add a single element to the end of a list.

# append():
# num = [1, 2, 3]
# num.append(4)        
# print(num)            

# extend() method: extend() is used to add multiple elements from an iterable to the end of a list.

# extend():
# num = [1, 2, 3]
# num.extend([4, 5])   
# print(num)




# 4..Write a Python function to get the largest number, smallest num and sum of all from a list.
# def get_stats(lst):
#     if not lst:
#         return None, None, 0

#     return max(lst), min(lst), sum(lst)

# # Example usage:
# my_list = [2, 33, 222, 14, 25]
# largest, smallest, total_sum = get_stats(my_list)
# print("Largest number:", largest)
# print("Smallest number:", smallest)
# print("Sum of all numbers:", total_sum)




# 5..How will you compare two lists?
# def lists_are_equal(list1, list2): 
   
#     if list1 == list2:
#         return True

#     if set(list1) == set(list2):
#         return True

#     if sorted(list1) == sorted(list2):
#         return True
    
#     return False

 


# 6..Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
 
# def count_strings_with_same_first_last_char(strings):
#     return sum(1 for s in strings if len(s) >= 2 and s[0] == s[-1])

# string_list = ['abca', 'xyz', 'aba', '1221']
# result = count_strings_with_same_first_last_char(string_list)
# print("Number of strings where first and last character are same:", result)




# 7..Write a Python program to remove duplicates from a list. 
# def remove_duplicates(input_list):
#     return list(set(input_list))

# input_list = [1, 2, 3, 4, 3, 2, 1]
# unique_list = remove_duplicates(input_list)
# print("List after removing duplicates:", unique_list)




# # 8..Write a Python program to check a list is empty or not.
# def empty_list(input_list):
#     return len(input_list) == 0

# list1 = []
# list2 = [1, 2, 3]

# print("Is list1 empty?", empty_list(list1))
# print("Is list2 empty?", empty_list(list2))




# 9..Write a Python function that takes two lists and returns true if they have
# at least one common member.
# def have_common_member(list1, list2):
#     for item in list1:
#         if item in list2:
#             return True
#     return False




# 10..Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30. 
# def generate_squares():
#     # Generate the list of squares
#     squares = [i**2 for i in range(1, 31)]
    
#     # Extract the first and last 5 elements
#     first_five = squares[:5]
#     last_five = squares[-5:]
    
#     return first_five, last_five

# # Main function
# if __name__ == "__main__":
#     first_five, last_five = generate_squares()
    
#     print("First 5 elements:", first_five)
#     print("Last 5 elements:", last_five)




# 11..Write a Python function that takes a list and returns a new list with unique
# elements of the first list. 
# def get_unique_elements(input_list):
#     seen = set()
#     unique_list = []
#     for item in input_list:
#         if item not in seen:
#             unique_list.append(item)
#             seen.add(item)
#     return unique_list

# # Example usage
# if __name__ == "__main__":
#     sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10]
#     unique_elements = get_unique_elements(sample_list)
    
#     print("Original list:", sample_list)
#     print("List with unique elements:", unique_elements)





# 12..Write a Python program to convert a list of characters into a string.
# def list_to_string(char_list):
#     # Use the join method to concatenate the list of characters into a string
#     result_string = ''.join(char_list)
#     return result_string

# # Example usage
# if __name__ == "__main__":
#     char_list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
#     result_string = list_to_string(char_list)
    
#     print("List of characters:", char_list)
#     print("Converted string:", result_string)





# 13..Write a Python program to select an item randomly from a list. 
# import random

# def select_random_item(input_list):
#     # Check if the list is not empty to avoid IndexError
#     if input_list:
#         # Use random.choice to select a random item from the list
#         return random.choice(input_list)
#     else:
#         return None  # Return None if the list is empty

# # Example usage
# if __name__ == "__main__":
#     sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     random_item = select_random_item(sample_list)
    
#     print("Original list:", sample_list)
#     print("Randomly selected item:", random_item)




# 14..Write a Python program to find the second smallest number in a list. 
# def second_smallest(numbers):
#     if len(numbers) < 2:
#         return "List must contain at least two elements"
    
#     smallest = float('inf')
#     second_smallest = float('inf')
    
#     for num in numbers:
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif num < second_smallest and num != smallest:
#             second_smallest = num
    
#     if second_smallest == float('inf'):
#         return "There is no second smallest element"
#     else:
#         return second_smallest

# # Example usage:
# numbers = [5, 3, 9, 2, 10, 7]
# print("Second smallest number:", second_smallest(numbers))





# 15..Write a Python program to get unique values from a list.
# def unique_values(lst):
#     unique_list = []
#     for item in lst:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# # Example usage:
# my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# print("Original list:", my_list)
# print("Unique values:", unique_values(my_list))




# 16..Write a Python program to check whether a list contains a sub list.
# def is_sublist(lst, sub_lst):
#     if len(sub_lst) == 0:
#         return True  # An empty list is always a sublist of any list
#     if len(sub_lst) > len(lst):
#         return False  # Sublist cannot be longer than the list
    
#     for i in range(len(lst) - len(sub_lst) + 1):
#         if lst[i:i+len(sub_lst)] == sub_lst:
#             return True
    
#     return False

# # Example usage:
# main_list = [1, 2, 3, 4, 5, 6, 7, 8]
# sub_list1 = [2, 3, 4]
# sub_list2 = [5, 6, 7, 8]
# sub_list3 = [9, 10]

# print("Main list:", main_list)
# print("Sublist 1:", sub_list1)
# print("Sublist 2:", sub_list2)
# print("Sublist 3:", sub_list3)

# print("Sublist 1 in main list:", is_sublist(main_list, sub_list1))
# print("Sublist 2 in main list:", is_sublist(main_list, sub_list2))
# print("Sublist 3 in main list:", is_sublist(main_list, sub_list3))





# 17..Write a Python program to split a list into different variables. 
# my_list = ["apple", "banana", "cherry"]

# # Assign elements to variables in order
# fruit1, fruit2, fruit3 = my_list

# print(fruit1)  # Output: apple
# print(fruit2)  # Output: banana
# print(fruit3)  # Output: cherry




# 18.What is tuple? Difference between list and tuple.

# A tuple in Python is an ordered, immutable collection of elements. Similar to a list, it 
# can hold various data types like numbers, strings, or even other lists. However, the
# key difference between lists and tuples is that tuples are immutable, meaning their
# elements cannot be changed after creation.

# List is mutable but tuple is immutable. List is enclosed in square brackets [], Tuple is enclosed in parentheses ().





# 19.Write a Python program to create a tuple with different data types. 
# # Create a tuple with string, integer, float, and boolean
# my_tuple = ("Hello", 42, 3.14, True)

# # Print the tuple
# print(my_tuple)

# # Print data types of elements (optional)
# print(type(my_tuple[0]))  # Output: <class 'str'>
# print(type(my_tuple[1]))  # Output: <class 'int'>
# print(type(my_tuple[2]))  # Output: <class 'float'>
# print(type(my_tuple[3]))  # Output: <class 'bool'>





# 20.Write a Python program to create a tuple with numbers. 
# # Create a tuple with numbers
# numbers_tuple = (1, 2, 3, 4, 5)

# # Print the tuple
# print(numbers_tuple)
