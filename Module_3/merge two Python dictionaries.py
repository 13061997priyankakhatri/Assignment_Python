'''
Write a Python script to merge two Python dictionaries.
'''

dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print("Merged Dictionary:", merged_dict)


