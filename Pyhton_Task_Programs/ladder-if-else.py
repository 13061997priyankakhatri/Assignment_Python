'''
marks1 = float (input ("Enter marks1 : "))

marks2 = float (input ("Enter marks2 : "))

marks3 = float (input ("Enter marks3 : "))

percentage = (marks1 + marks2 + marks3)/3

if percentage > 100:
    print("Inavaild marks")

elif percentage >= 90 and percentage <= 100:
    print("Grade A+")
    print(percentage)
    
elif percentage >= 80  :
    print("Grade B")
    print(percentage)
    
elif percentage >= 60  :
    print("Grade C")
    print(percentage)
    
elif percentage <= 40 and percentage > 0:
    print("Fail")
    
else:
    print("Invalid marks")
'''
"""
if marks1>marks2 and marks1>marks3:
    print("Marks1 is greater.")

elif marks2>marks1 and marks2>marks3:
    print("Marks2 is graeter.")

else:
    print("Marks3 is greater")
"""

number = int(input ("Enter number : "))

if number > 0:
    print("Number is positive.")

elif number == 0 :
    print("Number is zero.")

else:
    print("Number is negative.")
