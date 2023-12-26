def rectengle(l,w):
    return l * w
def triangle(h,b):
    return (0.5)* b * h
def circle(r):
    return 3.14 * r * r

choice = int(input("Enter your choice : "))
if choice == 1:
    l = int(input("Enter l : "))
    w = int(input("Enter w : "))
    print("Area of rectengle : ", rectengle(l,w))
elif choice == 2 :
    b = int(input("Enter b : "))
    h = int(input("Enter h : "))
    print("Area of triangle : ", triangle(h,b))
else:
    r = int(input("Enter r : "))
    print("Area if circle : ", circle(r))
