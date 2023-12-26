def sum_of_natural_numbers(number):
    if number <= 1:
        return 1
    else:
        return number + sum_of_natural_numbers(number - 1)
    
number = int(input("Enter number : "))
 
print("Sum of natural numbers : ", sum_of_natural_numbers(number))

