'''Write a Python program to test whether a passed
letter is a vowel or  not.'''

l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u') :
	print("%s is a vowel." % l)
	
elif l == 'y' :
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")

else :
	print("%s is a consonant." % l) 
	
