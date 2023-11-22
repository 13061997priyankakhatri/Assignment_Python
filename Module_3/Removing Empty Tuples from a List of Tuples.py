'''
Write a Python program to remove an empty tuple(s) from a list
of tuples. 
'''

list_of_tuples = [(), ('a', 'b'), (1,), ('x', 'y', 'z'), ()]

non_empty_tuples = [t for t in list_of_tuples if t]

print(non_empty_tuples)
