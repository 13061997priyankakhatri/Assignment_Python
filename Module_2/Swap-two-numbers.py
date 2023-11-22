'''Write python program that swap two number with
    temp variable and without temp variable.'''

number1 = 13
number2 = 6

print()
print("with third variable : ")

print("Before swapping : ",number1,number2)

temp = number1
number1 = number2
number2 = temp

print("After swapping : ",number1,number2)

print()
print("without third variable :")

print("Before swapping : ",number1,number2)

number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2

print("After swapping : ",number1,number2)
print()
