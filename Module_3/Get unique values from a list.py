'''
Write a Python program to get unique values from a list.
'''

def get_unique_values(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = get_unique_values(my_list)
print("Unique values:", unique_values)
