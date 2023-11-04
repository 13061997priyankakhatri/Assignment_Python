'''Write a Python program to get the
Factorial number of given number. '''

def factorial(num) : 

    if num == 1 or num == 0 :
        return 1
    
    else:
        return num * factorial(num - 1)
  
# Driver Code 
print()

num = int(input("Enter your number : "))

print()

print("Factorial :",factorial(num))

print()
