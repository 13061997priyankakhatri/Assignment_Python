'''
Write a Python function that checks whether a passed string is 
palindrome or not
'''

def is_palindrome(input_string):
    return input_string == input_string[::-1]

# Example usage:
test_string = "madam"
is_palindrome_result = is_palindrome(test_string.lower())
print(f"Is '{test_string}' a palindrome? {is_palindrome_result}")
