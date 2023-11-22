'''
Write a Python program to find the second smallest number in a
list.
'''

def second_smallest(input_list):
    unique_sorted = sorted(set(input_list))
    if len(unique_sorted) > 1:
        return unique_sorted[1]
    else:
        return "List doesn't have a second smallest element."

my_numbers = [5, 2, 8, 1, 3, 6]
result = second_smallest(my_numbers)
print("Second smallest number:", result)
