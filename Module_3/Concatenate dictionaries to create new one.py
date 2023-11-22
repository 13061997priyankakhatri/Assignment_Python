'''
Write a Python script to concatenate following dictionaries to
create a new one.
'''

dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}
dict3 = {'e': 500}

# Creating a new dictionary by concatenating all dictionaries
concatenated_dict = {**dict1, **dict2, **dict3}

print("Concatenated Dictionary:", concatenated_dict)



