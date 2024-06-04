# How can you get a random number in python?
import random

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print("Random integer between 1 and 10:", random_integer)

# Generate a random floating-point number between 5 and 10
random_float_uniform = random.uniform(5, 10)
print("Random float between 5 and 10:", random_float_uniform)

# Generate a random integer from a range
random_from_range = random.randrange(1, 10, 2)  # Random odd number between 1 and 10
print("Random number from range:", random_from_range)

# Pick a random element from a sequence
my_list = [1, 2, 3, 4, 5]
random_choice = random.choice(my_list)
print("Random choice from list:", random_choice)
