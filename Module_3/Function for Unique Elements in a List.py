'''
Write a Python function that takes a list and returns a new list
with unique elements of the first list. 
'''

def unique_elements(input_list):
    
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]

result = unique_elements(my_list)

print(result)
