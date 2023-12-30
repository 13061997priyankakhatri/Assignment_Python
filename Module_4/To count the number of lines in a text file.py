"""
Write a Python program to count the number of lines in a text file.
"""

file = open("umang.txt", "r")
Counter = 0

# Reading from file
Content = file.read()
List = Content.split("\n")

for p in List:
	if p:
		Counter += 1

print("This is the number of lines in the file")
print(Counter)

