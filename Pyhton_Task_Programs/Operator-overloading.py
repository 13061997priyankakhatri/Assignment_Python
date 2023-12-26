'''
task : use operator overloading concept

class A:
	pass
o1(12,3)
o2(12,3)

check that two instance are having idetical 
values or not ?

if both instance of class A having same value then return True
else return False
'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, person):
            return self.name == other.name and self.age == other.age
        return False

def check_equality(p1,p2):
    return p1 == p2

#creating instance of class person
p1 = person(13,6)
p2 = person(13,6)

#checking if both instances have identical values
answer = check_equality(p1, p2)
print(answer)
