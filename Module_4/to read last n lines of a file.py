"""
Write a Python program to read last n lines of a file. 
"""

# Make a single variable to store the path of the file. This is a constant value.
# This value must be replaced with the file path from your own system in the example below.
Filename = "umang.txt"

# Give the n value user input using the int(input()) function and store it in a variable.
given_n_value = int(input("Enter your number here : "))

# Open the file in read-only mode. In this case, we're simply reading the contents of the file.
with open(Filename, 'r') as filecontent:
    
    # Get all the lines of the file using the readlines() function
    lines_list= filecontent.readlines()
    print("The last",given_n_value,"lines of a given file are:")
    
    # Iterate in the above lines list using the for loop to get the last
    # n lines of a file using the negative indexing.
    for file_line in (lines_list[-given_n_value:]):
        
        # Print the last n lines of a given file.
        print(file_line, end ='')
