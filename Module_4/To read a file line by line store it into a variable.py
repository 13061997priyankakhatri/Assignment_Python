"""
Write a Python program to read a file line by line store it into a variable.
"""

def read_a_file(file_name):
    
        with open (file_name, "r") as file:
            
                info = file.readlines()
                print(info)
                
read_a_file('umang.txt')
