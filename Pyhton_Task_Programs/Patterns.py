A = 65
for i in range(5):
    for p in range(i+1):
        print(chr(A), end = " ")
        A += 1
    print()

print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

for i in range(5):
    A = 65
    for p in range(i+1):
        print(chr(A), end = " ")
        A += 1
    print()
    
print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

A = 65
for i in range(5):
    for p in range(i+1):
        print(chr(A), end = " ")
    A += 1
    print()

print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

N = 1
for i in range(0,6):
    for p in range(0,i + 1):
        print(N, end = " ")
        N += 1
    print()

print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

N = int(input("Enter number of lines of pettern: "))
for i in range(1,N+1):
    for p in range(1,i+1):
        print((p+1)%2, end = " ")
    print()
