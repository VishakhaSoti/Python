class Student:                #CLASS
    name = "Aman"

s1 = Student()                #OBJECT
print(s1.name)
#------------------------------------------------------------#

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database...")

s1 = Student("Ayush", 98)
print(s1.name, s1.marks)                  # self.name = s1.name

s2 = Student("Tashu", 90)
print(s2.name, s2.marks)
#------------------------------------------------------------#

class Student:                                  #CLASS
    college_name = "ABC College"                #CLASS.ATTR
    def __init__(self,name, marks):             #CONSTRUCTOR
        self.name = name                        #OBJECT ATTR
        self.marks = marks                      #OBJECT ATTR

    def welcome(self):                          #METHOD1
        print("welcome student", self.name)

    def get_marks(self):                        #METHOD2      
        return self.marks

s1 = Student("Ridhi", 89)                       #OBJECT 
s1.welcome()                                    #CALLED METHOD1
print(s1.name, s1.marks, s1.college_name)       
print(s1.get_marks())                          #CALLED METHOD2 
#---------------------------------------------------------------------#

#PRACTICE QUES

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hello,", self.name, "your average score is: ", sum/3)

s1 = Student("Ayush", [94,98,96])
s1.avg()

s2 = Student("Tashu", [93,97,95])
s2.avg()
#---------------------------------------------------------------------#
