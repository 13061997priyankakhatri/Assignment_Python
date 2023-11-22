'''
Write a Python program to replace last value of tuples in a list.
'''

list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

modified_list = [t[:-1] + (100,) for t in list_of_tuples]

print(modified_list)
