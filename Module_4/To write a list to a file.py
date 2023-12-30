"""
Write a Python program to write a list to a file.
"""

List = [13,6,12,12,5,9,30,10]

with open('umang.txt', 'w') as file:
    
  file.write('\n'.join(str(p) for p in List))
