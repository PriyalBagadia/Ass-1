# Write python program that user to enter only odd numbers, else will raise an exception.

def get_odd_number():
    while True:
        try:
            number = int(input("Enter an odd number: "))
            if number % 2 != 0:
                return number
            else:
                raise ValueError("Please enter an odd number.")
        except ValueError as ve:
            print(ve)

try:
    odd_number = get_odd_number()
    print("You entered an odd number:", odd_number)
except KeyboardInterrupt:
    print("\nProgram terminated by the user.")
