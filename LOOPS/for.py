list = [1,2,3,4]

for el in list:
    print(el)
#-------------------#
str = "APPLE"

for el in str:
    print(el)
else:
    print("end")
#-------------------#
str1 = "orange"
for el in str1:
    if(el == "a"):
        print("a found")
        break
    print(el)

print("END")
#--------------------------------------#
nums = (1,4,9,16,25,36,49,64,81,100,16)

x = 16
idx = 0
for el in nums:
    if(el == x):
        print("found at idx", idx)
    idx +=1
print("END") 
#--------------------------------------#
#RANGE

for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(1, 10, 2):    #start?,stop,step?
    print(i)

n = int(input("enter any number:"))
for i in range(1, 11):
    print(n*i)