number1 = 13
number2 = 6

'''

#with third variable

print("Before swapping : ",number1,number2)

temp = number1
number1 = number2
number2 = temp

print("After swapping : ",number1,number2)

'''

#without third variable

print("Before swapping : ",number1,number2)

number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2

print("After swapping : ",number1,number2)
