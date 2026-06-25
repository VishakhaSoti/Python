#STATIC METHOD

class Student:
    @staticmethod                   #DOES NOT USE SELF PARAMETER
    def college():
        print("ABC College")
s1 = Student()
s1.college()
#---------------------------------------------------------------------#

#CLASS METHOD

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):         #USES CLS FOR CLASS
        cls.name = name

p1 = Person()
p1.changeName("Ritik")
print(p1.name)
print(Person.name)
#---------------------------------------------------------------------#

#PROPERTY DECORATOR

class Student:
    def __init__(self, phy, chem, bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    @property                                 #PROPERTY DECORATOR
    def percentage(self):
        return str((self.phy + self.chem + self.bio) /3) + "%"
    
stu1 = Student(88,97,67)
print(stu1.percentage)
stu1.bio = 93
print(stu1.percentage)
#---------------------------------------------------------------------#