'''
Write a Python program to find the highest 3 values in a
dictionary.
'''

def highest_3_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1],
                          reverse=True)
    return dict(sorted_items[:3])

# Sample dictionary
sample_dict = {'a': 100, 'b': 300, 'c': 150, 'd': 75, 'e': 500}
highest_values = highest_3_values(sample_dict)
print(highest_values)

