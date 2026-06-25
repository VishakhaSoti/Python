#SINGLE INHERITANCE

class Car:                            #PARENT CLASS
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")
    
class ToyotaCar(Car):                   #CHILD CLASS
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print(car1.name)
print(car1.start())
#----------------------------------------------------------------------#

#MULTI LEVEL INHERITANCE

class Car:                            #PARENT CLASS 1
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):                 #CHILD CLASS 1/ PARENT CLASS 2
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):           # CHILD CLASS 2
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
print(car1.type)
car1 = ToyotaCar("Prius")
print(car1.brand)
car1.start()
car1.stop()
#----------------------------------------------------------------------#

#MULTIPLE INHERITANCE

class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"

s1 = C()
print(s1.varA)
print(s1.varB)
print(s1.varC)
#----------------------------------------------------------------------#

#SUPER METHOD IN INHERITANCE

class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")
    
class TataCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = TataCar("Safari", "Petrol")
print(car1.name, car1.type)
car1.stop()