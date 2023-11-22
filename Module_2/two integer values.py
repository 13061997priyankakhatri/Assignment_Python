'''
Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5.
'''

# Define a function 'test_number5' that takes two integer inputs: p and u.
def test_number5(p, u):
    
    # Check if any of the following conditions are met:
    # 1. x is equal to y.
    # 2. The absolute difference between x and y is equal to 5.
    # 3. The sum of x and y is equal to 5.
    
    if p == u or abs(p - u) == 5 or (p + u) == 5 :
        # If any of the conditions are met, return True.
        return True
    
    else:
        # If none of the conditions are met, return False.
        return False

'''Test the 'test_number5' function with different sets of input values and
print the results.'''

print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))
