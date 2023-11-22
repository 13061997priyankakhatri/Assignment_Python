'''Write a Python program to sum of three given
integers. However, if two values are equal sum will be
zero.'''

'''Define a function named "sum_thrice" that takes
three integer parameters : p, u and n'''

def sum_thrice(p, u, n) :
    # Calculate the sum of p, u and n
    sum = p + u + n

    # Check if p, u and n are all equal (all three numbers are the same)
    if p == u == n :
        
        # If they are equal, triple the sum
        sum = sum * 3

    # Return the final sum
    return sum

'''Call the "sum_thrice" function with the arguments
(13, 6, 10) and print the result'''

print(sum_thrice(13, 6, 10))

'''Call the "sum_thrice" function with the arguments
(12, 30, 12) and print the result'''

print(sum_thrice(12, 30, 12))
