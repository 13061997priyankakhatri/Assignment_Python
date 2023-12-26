'''
Task : Take input from user in file and count how many words are there
in file.
'''

# open the file in read mode
file_name = input("Enter the file name : ")

try:
    with open(file_name, 'r') as file:
        # Read the content of the file
        content = file.read()
        
        # Split the content into words
        words = content.split()
        
        # Count the number of words
        number_of_words = len(words)
        
        print(f"The file '{file_name}' has {number_of_words} words.")
        
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
except IOError:
    print("An error occurred while reading the file.")

else:
    print("Try to catch this block")

finally:
    print("This is always executed.")
