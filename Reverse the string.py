"""
Write a Python function to reverses a string if its
length is a multiple of 4.
"""

def reverse_string(string1) :
    
    if len(string1) % 4 == 0 :
        
       return ''.join(reversed(string1))

    return string1

print(reverse_string("Jethannd"))

print(reverse_string("Priyanka"))
