'''
Write a Python program to unzip a list of tuples into
individual lists. 
'''

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*list_of_tuples)

print(list(numbers))

print(list(letters))
