# How Do You Check The Presence Of A Key In A Dictionary?

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using 'in' operator
if 'a' in my_dict:
    print("'a' exists in the dictionary.")

# Using 'get()' method
if my_dict.get('z') is not None:
    print("'z' exists in the dictionary.")