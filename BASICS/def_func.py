def add():
    a = 10
    b = 20
    c = a+b
    print("sum of a and b is", c)
add()
#----------------------------------------------#
def add(x,y):
    z= x+y
    print(z)
add(10,15)
#----------------------------------------------#
def calc_prod(a, b=2):
    print(a*b)
    return a*b
calc_prod(2)
#----------------------------------------------#

cities = ['mumbai', 'delhi', 'pune', 'noida']
heroes = ['spiderman', 'thor', 'ironman']

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)        #printing len of list
#----------------------------------------------#

cities = ['mumbai', 'delhi', 'pune', 'noida']

def print_list(list):
    for i in list:
        print(i, end=" ")

print_list(cities)      #printing items of list in single line
print()
#--------------------------------------------------------------#
#RECURSIVE FUNCTION

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)