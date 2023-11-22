'''
Write a Python script to print a dictionary where the keys are
numbers between 1 and 15. 
'''

num_dict = {num: num*num for num in range(1, 16)}
print("Dictionary with keys as numbers from 1 to 15:", num_dict)
