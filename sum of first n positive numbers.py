'''Write a python program to sum of the
first n positive integers.'''

'''Prompt the user for input and convert
it to an integer.'''

p = int(input("Input a number: "))

'''Calculate the sum of the first 'n'
positive integers using the formula.'''

sum_num = (p * (p + 1)) / 2

'''Print the result, indicating the sum
of the first 'n' positive integers.'''

print("Sum of the first", p, "positive integers:", sum_num)
