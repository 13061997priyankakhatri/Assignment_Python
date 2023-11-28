"""
    Strings :

        representative with 'Hello', "Hello",'''Hello'''

        Inbuilt class : str()

        --> Characteristics :

            - They are indexible : Starts from zero
            - They support negative indexing
            - They are Mutable / Changeble
            - They are iterable
            
"""

string = input("Enter any string:")

character = input("Enter any character:")

ch_freq = 0
counter = 0    
for p in string:
    counter = counter + 1
    print("Counter is :",counter)
    if character == p:
        ch_freq += 1

print("Frequency is : ",ch_freq)


print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

STRING1 = 'Welcome to Palanpur'
STRING2 = "Welcome to Bhuj"
STRING3 = """

            ----------------- Hello Python ----------------

            -> Functions
            -> Strings
            -> Lists
            -> Dictionaries
            -> Conditional Statements
"""

print("String1 is : ",STRING1)
print(type(STRING1))

print("String2 is : ",STRING2)
print(type(STRING2))
    
print("String3 is : ",STRING3)
print(type(STRING3))
