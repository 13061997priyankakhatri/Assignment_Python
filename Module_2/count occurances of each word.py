'''Write a Python program to count the occurrences
of each word in a given sentence.'''

string = input("Enter string : ")
word = input("Enter word : ")

p = []

count = 0

p = string.split(" ")

for i in range(0,len(p)) :
    
      if(word == p[i]) :
            count=count+1
            
print("Count of the word is : ")
print(count)
