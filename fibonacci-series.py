'''Write a Python program to get the Fibonacci series of given range.'''

Nth = int(input("How many terms? "))

# first two terms

n1, n2 = 0, 1

count = 0

# check if the number of terms is valid

if Nth <= 0 :
   
   print()

   print("Please enter a positive integer")

# if there is only one term, return n1

elif Nth == 1 :
   
   print()

   print("Fibonacci sequence upto",Nth,":")

   print()

   print(n1)

# generate fibonacci sequence

else :
   
   print()

   print("Fibonacci sequence:")

   print()

   while count < Nth :
       
       print(n1)

       nth = n1 + n2

       # update values

       n1 = n2
       n2 = nth
       
       count += 1

print()
