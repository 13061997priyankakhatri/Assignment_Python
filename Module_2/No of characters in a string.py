'''Write a Python program to count the number of
characters (character frequency) in a string.'''

string = input("Enter any string:")

character = input("Enter any character:")

ch_freq = 0

counter = 0

for p in string :
    
    counter = counter + 1
    print("Counter is :",counter)
    
    if character == p :
        ch_freq += 1

print("Frequency is : ",ch_freq)
