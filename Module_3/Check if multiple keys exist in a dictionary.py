'''
Write a Python program to check multiple keys exists in a
dictionary.
'''

my_dict = {'a': 1, 'b': 2, 'c': 3}

keys_to_check = ['a', 'b', 'd']
if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("One or more keys are missing in the dictionary.")
