print()
Dict_1 ={"name" : "Priyanka","age" : 26, "canvote" : True}
print(Dict_1)

print()
<<<<<<< HEAD
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()
'''
=======
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()

>>>>>>> a48689eba83e596409e192e3b7e856da88760e37
Dict2 = {}
alnum = input("Enter email : ")
for p in range(15):
    Dict2[alnum[p]]= p
print("Email is:", Dict2)

print()
Dict3 = {}
alpha = input("Enter password :")
for u in range(0,8):
    Dict3[alpha[u]]= u 
print("Password is:", Dict3)
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()

Tops = {}

name = input("Enter student name : ")
id = input("Enter student id : ")

Tops['Student'] = {'name':name,'id':id}

course_name = input("Enter course name : ")
fees = int(input("Enter course fees : "))

Tops['Courses'] = {'course_name':course_name,'fees':fees}

name = input("Enter faculty name : ")
id = input("Enter faculty id : ")

Tops['Feculty'] = {'name':name,'id':id}

print(Tops)

print()
<<<<<<< HEAD
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()
'''

# task : if keys are same then make addition of values
'''
Dict_1 ={"name" : "Priyanka","age" : 26, "canvote" : True}
Dict_2 ={"name" : "Priyanka","age" : 20, "canvote" : True}

Dict_1.update(Dict_2)
print(Dict_1)

print()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()

# task : make sorting of dictionary based on values

Dict_1 ={"name" : "Priyanka","age" : 26, "canvote" : True}
sortedDict_1 = sorted(Dict_1)

print(sortedDict_1)

print()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()
'''
=======
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()

>>>>>>> a48689eba83e596409e192e3b7e856da88760e37
Quiz_game = {}

for p in range(1,11) :
    
    que = input("Enter your question : ")
    ans = input("Enter your answer : ")
<<<<<<< HEAD
    Quiz_game.update({str(p) :{"que": que , "ans": ans}})
    
print("Quiz_game = ",Quiz_game)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")        

points = 0

i = 1

while i <= 10 :
    
    print("que " + str(i) + " : " + Quiz_game[str(i)]["que"])
    user_ans = input("Enter your answer : ")
    
    if (Quiz_game[str(i)]["ans"]) == user_ans :
        
        print("Your answer is right.You got 10 points.")
        points += 10
        print("Final score is : ", points)
        
    else:
        
        print("Your answer is wrong.You got -5 points.")
        points -= 5
        print("Final score is : ", points)
        
    i += 1

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()
=======

    Quiz_game.update({"que"+str(p) :{"que": que , "ans": ans}})

print("Quiz_game = ",Quiz_game)

print()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print()

# task : if keys are same then make addition of values

Dict_1 ={"name" : "Priyanka","age" : 26, "canvote" : True}
Dict_2 ={"name" : "Priyanka","age" : 20, "canvote" : True}

Dict_1.update(Dict_2)
print(Dict_1)
>>>>>>> a48689eba83e596409e192e3b7e856da88760e37
