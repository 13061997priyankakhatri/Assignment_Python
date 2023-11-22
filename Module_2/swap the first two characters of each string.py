'''Write a Python program to get a single string from
two given strings, separated by a space and swap
the first two characters of each string.'''

p = "Priyanka"
u = "Umang"

print("Before Swap :",p," ",u)

p1 = u[:2] + p[2:]
u1 = p[:2] + u[2:]

print("After Swap :",p1," ",u1)
