number = int(input("Enter your prime number : "))
if number <= 1 :
    print("Not prime.")
if number > 1 :
    for p in range(2,number):
        if number % p == 0 :
            print("Not prime.")
            break
    else:
        print("Prime.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print()
first_number = int(input("Enter your first number : "))
last_number = int(input("Enter your last number : "))
print()
for number in range(first_number, last_number + 1) :
    if number >= 1 :
        for p in range(2, number) :
            if number % p == 0 :
                break
        else :
            numbers = list()
            while(number := int(input("Enter your number:"))) != 0:
                numbers.append(number)
            print(numbers)
            
print()
