"""
Write a Python program to count the frequency of words in a file.
"""

from collections import Counter

def count_words(file_name):
    
        with open(file_name) as file:
                return Counter(file.read().split())

print("Number of words in the file :",count_words("umang.txt"))
