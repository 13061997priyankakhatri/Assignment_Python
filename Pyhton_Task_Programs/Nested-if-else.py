number1 = int(input("Enter number1 : "))

number2 = int(input("Enter number2 : "))

number3 = int(input("Enter number3 : "))

'''
if number1 > number2:
    print("Number1 is greater.")
    
    if number2 > number3:
        print("Number2 is greater.")
        
        if number3 > number1:
            print("Number3 is greater.")
            
        else:
            print("Number3 is smaller.")
    else:
        print("Number2 is smaller.")
else:
    print("Number1 is smaller.")
'''

if number1>number2:
    if number1>number3:
        print("Number1 is greater.")

    else:
        print("Number3 is greater.")
else:
    if number2 > number3:
        print("Number2 is greater.")

    else:
        print("Number3 is greater.")
    
