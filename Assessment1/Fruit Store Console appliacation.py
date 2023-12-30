# Fruit Store Console Application

print()
Fruit_Market = 'WELCOME TO FRUIT MARKET\n'
print(Fruit_Market.center(60, " "))

# Menu of the program
Menu = "1) Manager "
print(Menu.center(60," "))
Menu1 = "2) Customer\n"
print(Menu1.center(60, " "))

# Select the Role
ch = int(input('Select your role : '))
print()
dict_main = {}

def Main_menu():
    Manager = "Fruit Market Manager\n"
    print(Manager.center(60, " "))

    # If-Else Statement
    if ch == 1:
        Stoke1 = "1) Add Fruit Stoke"
        print(Stoke1.center(55, " "))
        Stoke2 = "2) View Fruit Stoke"
        print(Stoke2.center(57, " "))
        Stoke3 = "3) Update Fruit Stoke\n"
        print(Stoke3.center(60, " "))

    else: 
        print('Invalid role')

    print()
    choice = int (input ("Enter your choice : "))  

    # If-elif-else Statement
    if choice == 1 :
        
        dict_info = {}
        print("ADD FRUIT STOKE")
        fruit = input("Enter fruit Name : ")
        qty = int(input('Enter Qty : '))
        price = int(input('Enter Price (for kg): '))
        
        dict_info.update({'qty' : qty })
        dict_info.update({'price' : price })
        dict_main.update({fruit : dict_info})

    elif choice == 2 :

        print("VIEW FRUIT STOKE")
        print(dict_main)

    else:

        print("UPDATE FRUIT STOKE")
        dict_info = {}
        
        fruit = input("Enter fruit Name : ")
        qty = int(input('Enter Qty : '))
        price = int(input('Enter Price (for kg): '))
        dict_info.update({'qty' : qty })
        dict_info.update({'price' : price })

        dict_main.update({fruit : dict_info})
        
    # To Continue the Program with this Function
    continue_function = int(input("Do you want to perform more operations ? (if yes press 1 else press 0) : "))
    print()

    # If Statement 
    if(continue_function == 1 ):
        Main_menu()
    
    # Return Statement
    return

# Call the Function
Main_menu()
