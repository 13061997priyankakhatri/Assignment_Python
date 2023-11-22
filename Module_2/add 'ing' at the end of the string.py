"""Write a Python program to add 'ing' at the end
of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string
is less than 3, leave it unchanged."""

def string(string1):
    
  length = len(string1)

  if length > 2 :
      
    if str1[-3:] == 'ing' :
        
      str1 += 'ly'
      
    else :
        
      str1 += 'ing'

  return str1

print(add_string("Pr"))

print(add_string("Umang"))

print(add_string("Writing"))
