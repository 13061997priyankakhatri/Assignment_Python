'''
Write a Python program to count the number of strings where the
string length is 2 or more and the first and last character are
same from a given list of strings.
'''

def count_strings(input_list):
    
    count = 0

    for word in input_list:

        if len(word) >= 2 and word[0] == word[-1]:

            count += 1

    return count

words_list = ['abca', 'xyz', 'noon', 'level']

result = count_strings(words_list)

print("Count of strings:", result)
