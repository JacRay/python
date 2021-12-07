class student:
    name = 'Tim'
    age = 21
    gender = 'male'

#student is inherited to person 
# can use import to inhertit from other file

class person(student):
    pass 
p1 = person()
print(p1.name)
