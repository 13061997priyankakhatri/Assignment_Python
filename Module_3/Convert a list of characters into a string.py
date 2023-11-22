'''
Write a Python program to convert a list of characters into a
string.
'''

# Method 1: Using join()
char_list = ['a', 'b', 'c', 'd', 'e']
string_from_list = ''.join(char_list)
print(string_from_list)

# Method 2: Using str()
string_from_list = str(char_list).strip('[]').replace(", ", "")
print(string_from_list)
