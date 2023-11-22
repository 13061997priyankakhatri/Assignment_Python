"""Write a Python program to find the first appearance
of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'..
'poor' substring with 'good'. Return the resulting
string. """

def not_poor(string1):
  string_not = string1.find('not')
  string_poor = string1.find('poor')
  

  if string_poor > string_not and string_not > 0 and string_poor > 0 :
      
    string1 = string1.replace(string1[string_not:(string_poor + 4)], 'good')

    return string1

  else :
      
    return string1

print(not_poor('The song is not that poor!'))
print(not_poor('The song is poor!'))
