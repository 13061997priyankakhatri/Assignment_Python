def sum_of_natural_numbers(number):
    if number <= 1:
        return number
    else:
        return number + sum_of_natural_numbers(number - 1)
print()
number = int(input("Enter number : "))
print()
if number <= 0 :
    print("Please enter positive number.")
else:
    print("Sum of natural numbers : ", sum_of_natural_numbers(number))
print()


