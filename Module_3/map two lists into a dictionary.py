'''
Write a Python program to map two lists into a dictionary.
'''

def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example usage:
list1 = ['a', 'b', 'c']
list2 = [100, 200, 300]
result_dict = map_lists_to_dict(list1, list2)
print(result_dict)
