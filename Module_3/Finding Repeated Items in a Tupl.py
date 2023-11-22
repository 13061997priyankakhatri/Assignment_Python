'''
Write a Python program to find the repeated items of a tuple.
'''

my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)

repeated_items = {x for x in my_tuple if my_tuple.count(x) > 1}

print(repeated_items)
