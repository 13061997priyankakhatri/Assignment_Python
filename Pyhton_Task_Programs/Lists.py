'''

    List : "Collection that can store one or more value of diff. data type"

    represents with : []
    inbuilt-class : list

    >>List Array Diff

    List is having multiple elements of multiple data types
    Array can have multiple elements of same data type

    >>Characteristics : 

        - Lists are mutable/changable
        - List support -ve indexing
        - List is orderable
        - Lists are iterable

'''

print()
list1 = []  # blank list

list2 = list()  # blank list

print(list1)
print(type(list1))
print(id(list1))

print(list2)
print(type(list2))
print(id(list2))
print()

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print()
List3 = [13.6,30,10,5,9,12.12,True,None,"Priyanka"]
print(List3)

for p in List3 :
    print(p)

# List Slice

print(List3[:])

print(List3[::-1])

List3.reverse() # inplace change occur
print(List3)
print()

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print()
Subjects = ["Maths" , "English", "Science",
            "Physics", "Chemistry", "Computer",
            "History", "Social Science"]
Subjects.sort(reverse=True)
print("Decending Sorting is :",Subjects)
print()

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

list1 = [12,34,65,12,45,7,34,65,67,45]
#WAP to remove duplicate elements.

list1.remove(12)
print(list1)

list1.remove(65)
print(list1)

list1.remove(45)
print(list1)

list1.remove(34)
print("Remove method is :",list1)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print()
list1 = []

list1.extend([22,45,56,90,67,89,56,78,89,90])
print("Extend method is : ",list1)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print()

list4 = []

for p in range(0,10):
    number = int(input(f"Enter number {p+1} :"))
    list4.append(number)

print(list4)

unique_list = []

for element in list4 :
    if element not in unique_list :
        unique_list.append(element)
print("Unique list is : ",unique_list)      

