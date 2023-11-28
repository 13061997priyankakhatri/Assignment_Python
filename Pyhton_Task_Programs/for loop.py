Number = int(input("Enter number : "))
for n in range(1,11):
    print(Number,"x",n,"=",(6 * n))
print()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")    

print()
for j in range(4):
    for p in range(4):
        print(" * ",end = " ")
    print()
print()

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print()
for j in range(5):
    for p in range(5):
        if j==2 and p==2 :
            print(" $ ",end = " ")
        else:
            print(" * ",end = " ")
            
    print()
print()

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print()
for j in range(5):
    for p in range(5):
        if j==p :
            print(" $ ",end = " ")
        else:
            print(" * ",end = " ")
            
    print()
print()

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print()
for j in range(1,6):
    for p in range(1,j+1):
        if j==p :
            print(" $ ",end = " ")
        else:
            print(" * ",end = " ")
            
    print()
print()

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print()
for j in range(5):
    for p in range(5):
        if j==p :
            print(" $ ",end = " ")
        else:
            print(" * ",end = " ")
            
    print()
print()
