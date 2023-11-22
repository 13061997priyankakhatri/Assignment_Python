'''
Write a Python function to get the largest number, smallest num
and sum of all from a list.
'''

def list_operations(input_list):
    
    largest = max(input_list)
    
    smallest = min(input_list)
    
    total_sum = sum(input_list)
    
    return largest, smallest, total_sum

list1 = [13, 6, 5, 9, 30, 10, 12, 12]

result = list_operations(list1)

print("Largest:", result[0])

print("Smallest:", result[1])

print("Sum:", result[2])
