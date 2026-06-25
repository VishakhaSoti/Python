#CREATING PRIVATE ATTRIBUTES

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no                #PUBLIC OBJECT ATTR, CAN BE USED OUTSIDE THE CLASS
        self.__acc_pass = acc_pass          #PRIVATE OBJECT ATTR, CANNOT BE USED OUTSIDE THE CLASS, BUT WITHIN THE CLASS

    def reset(self):
        print(self.__acc_pass)

acc1 = Account(12345, "abcd")
print("account number: ", acc1.acc_no)
print("reset password: ", acc1.reset())           
print("account password: ", acc1.__acc_pass)    
#----------------------------------------------------------------------------------#

class Person:
    __name = "anonymous"           #PRIVATE CLASS ATTRIBUTE

p1 = Person()
print(p1.name)
#----------------------------------------------------------------------------------#

#CREATING PRIVATE METHOD

class Car:
    def __hello(self):              #PRIVATE METHOD
        print("hello car!")          

    def welcome(self):             #PUBLIC METHOD
        self.__hello()

c1 = Car()
print(c1.welcome())
#---------------------------------------------------------------------#