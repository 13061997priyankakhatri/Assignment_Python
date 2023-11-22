'''
Write a Python script to check if a given key already exists in a
dictionary. 
'''

my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'b'
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
