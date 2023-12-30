'''
Write a Python program to read first n lines of a file. 
'''

# input text file
fileName = "umang.txt"

# Create user input
Number = int(input("Enter your number here : "))

# Opening the given file in read-only mode
with open(fileName, 'r') as file:

    # Read the file lines using readlines() 
    Lines= file.readlines()
    print("The following are the first",Number,"lines of a text file:")

    # Traverse in the list of lines to retrieve the first n lines of a file
    for text in (Lines[:Number]):

        # Printing the first n lines of the file line by line.
        print(text, end ='')

    # Closing the input file
    file.close()
