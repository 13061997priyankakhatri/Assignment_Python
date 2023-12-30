"""
Write a Python program to copy the contents of a file to another file.
"""

# open both files 
with open('umang.txt','r') as file1, open('priyanka.txt','a') as file2: 
	
    # read content from first file 
    for line in file1: 
			
       # append content to second file 
       file2.write(line)
