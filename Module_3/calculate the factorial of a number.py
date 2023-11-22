'''
Write a Python function to calculate the factorial of a number (a 
nonnegative integer) 
'''


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage:
number = 6
factorial_result = factorial(number)
print(f"The factorial of {number} is: {factorial_result}")
