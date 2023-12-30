"""
Write a Python program to read a file line by line and store it into a list.
"""

with open('umang.txt') as file:
	lines = file.readlines()

print(lines)

# removing the new line characters
with open('umang.txt') as file:
	lines = [line.rstrip() for line in file]

print(lines)
