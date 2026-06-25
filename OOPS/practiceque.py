class Account:
    
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc
    
    def debit(self, amount):                                    #DEBIT
        self.balance -= amount
        print("Rs.", amount, "was debited...")
        print("Current Balance = ", self.get_balance())
    
    def credit(self, amount):                                   #CREDIT
        self.balance += amount
        print("Rs.", amount, "was credited...")
        print("Current Balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
#-----------------------------------------------------------------------------------#

class Circle:

    def __init__(self, r):                           #RADIUS
        self.radius = r

    def get_area(self):                              #AREA OF CIRCLE
        area = 3.14*self.radius**2
        print("area of circle is: ", area)
    
    def get_perimeter(self):                         #PERIMETER OF CIRCLE
        perimeter = 2*3.14*self.radius
        print("perimeter of circle is: ", perimeter)

r1 = Circle(7)
r1.get_area()
r1.get_perimeter()
#-----------------------------------------------------------------------------------#

class Employee:                                              #PARENT CLASS
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails1(self):                                   #METHOD 
        print("role: ", self.role)
        print("dep: ", self.dept)
        print("salary: ", self.salary)

class Engineer(Employee):                                    #CHILD CLASS
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "70,000")         #SUPER METHOD

    def showDetails2(self):                                  #METHOD
        print("name: ", self.name)
        print("age: ", self.age)


eng1 = Engineer("Ayush", "22")
eng1.showDetails1()
eng1.showDetails2()

eng2 = Employee("Data Analyst", "IT", "60,000")
eng2.showDetails1()
#-----------------------------------------------------------------------------------#