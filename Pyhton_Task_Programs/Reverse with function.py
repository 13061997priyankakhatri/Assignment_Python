def reverse(number):    
    if number >= 0 :
        print(number)
        return reverse(number - 1)
    else:
        return 0
print()
number = int(input("Enter number : "))
print()
print("Reverse numbers are : ")
print()
reverse(number)
