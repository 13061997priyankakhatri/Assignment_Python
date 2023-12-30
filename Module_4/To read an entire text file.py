'''
Write a Python program to read an entire text file.

==> Reading from a File :

    -> This is the default mode if no mode is passed as a parameter.

    -> Once we have a file object, we can use various methods to read from the file.

    -> The read() method reads the entire contents of the file and returns it as a string.

    -> This mode opens the file for reading only and gives an error if the file does not exist. 
'''

p = open('umang.txt')

Important = p.read()
print(Important)

p.close()
