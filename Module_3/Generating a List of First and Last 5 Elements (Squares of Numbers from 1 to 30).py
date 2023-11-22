'''
Write a Python program to generate and print a list of first and
last 5 elements where the values are square of numbers between
1 and 30.
'''

numbers = list(range(1, 31))

squares = [i ** 2 for i in numbers]

result = squares[:5] + squares[-5:]

print(result)
