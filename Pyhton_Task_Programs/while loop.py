'''

    initialization
    while condition:
        code...
        updation
        
    >>It is an Entry / Execution Control loop
    
'''

p = True

while p:
    number = int(input("Enter number: "))

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    choice = input("Want to contonue ? ['Y / N'] :")

    if choice == 'Y' :
        p = True
    else:
        p = False
        
