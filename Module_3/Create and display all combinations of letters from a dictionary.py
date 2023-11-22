'''
Write a Python program to create and display all combinations of
letters, selecting each letter from a different key in a
dictionary. 

Sample data: {'1': ['a','b'], '2': ['c','d']} 

Expected Output: 
ac ad bc bd
'''

from itertools import product

def combinations_from_dict(dictionary):
    values = list(dictionary.values())
    combinations = list(product(*values))
    for combo in combinations:
        print(''.join(combo), end=' ')

# Sample data
data = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations_from_dict(data)


