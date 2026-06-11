num = 9

if num % 2 == 0:
    print("even")
else:
    print("odd")

#-----------------------#

a = 5
b = 6
c = a+b

if c>=15:
    print("yes")
else:
    print("no")
#-----------------------#

food = input("food: ")
eat = "Yes" if food == "cake" else "No"
print(eat)
#-------------------------------------------------------------------------#

food = input("food: ")
print("sweet") if food == "cake" or "jalebi" else print("not sweet")

#--------------------------------------------------------------------------#
sal = int(input("salary: "))

if sal >= 50000:
    tax = sal*0.2
    print("the tax is:", tax)
else:
    tax = sal*0.1
    print("the tax is",tax)