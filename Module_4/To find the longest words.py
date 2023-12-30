"""
Write a python program to find the longest words.
"""

def longest_word(filename):
    
    with open(filename, 'r') as file:
              words = file.read().split()
              
    maximum_length = len(max(words, key=len))
    
    return [word for word in words if len(word) == maximum_length]

print(longest_word('umang.txt'))
