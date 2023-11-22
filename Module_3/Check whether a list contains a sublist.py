'''
Write a Python program to check whether a list contains a
sub list

'''

def contains_sublist(main_list, sublist):
    return all(item in main_list for item in sublist)

list1 = [1, 2, 3, 4, 5]
sub_list = [2, 3]
if contains_sublist(list1, sub_list):
    print("List contains the sub list")
else:
    print("List does not contain the sub list")
