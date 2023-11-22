'''
Write a Python function that takes two lists and returns true if
they have at least one common member. 
'''

def common_member(list1, list2):
    
    for item in list1:

        if item in list2:

            return True

    return False

list_a = [1, 2, 3]

list_b = [3, 4, 5]

result = common_member(list_a, list_b)

print(result)
