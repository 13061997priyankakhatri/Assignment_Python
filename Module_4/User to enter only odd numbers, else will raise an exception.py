"""
Write python program that user to enter only odd numbers, else will 
raise an exception.
"""


class OddNumberException(Exception):
    pass

def get_odd_number():
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise OddNumberException("Entered number is even.")
    except ValueError:
        raise OddNumberException("Invalid input. Please enter a number.")
    else:
        return number

try:
    odd_number = get_odd_number()
    print(f"You entered an odd number: {odd_number}")
    
except OddNumberException as e:
    print(f"Error: {e}")

	
