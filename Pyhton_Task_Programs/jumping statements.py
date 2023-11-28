"""
    Jumping Statements:

        Break : Will break the iteration

        Continue : Will Skip the iteration and continue from next

        Pass : To do Nothing

"""

for p in range(7):
    if p == 7 :
        break
    print(p)

print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

for p in range(13):
    if p == 7 :
        continue
    print(p)

print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

for p in range(13):
    pass
    print(p)
