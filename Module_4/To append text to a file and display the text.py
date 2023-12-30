'''
Write a Python program to append text to a file and display the text.

==> If you want to append to a file instead of overwriting it, you can open it in append mode.
'''

def files(name):
    from itertools import islice
    with open(name, "w") as file :
        file.write('Hello Python!')
        file.write('Hello Django!')
    text = open(name)
    print(text.read())
files('umang.txt')
