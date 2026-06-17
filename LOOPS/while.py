i = 1
while i <= 5:
    print("Vishakha", i)
    i +=1
 #--------------------------#

i = 1
while i<=5:
    print(i)
    i +=1
 #--------------------------#

i = 5
while i>=1:
    print(i)
    i -=1 
#--------------------------#

i = 1
while i <=10 :
    print(3*i)        #(n*i), constant * variable
    i += 1

n = int(input("Enter a num: "))
i = 1
while i<=10:
    print(n*i)
    i +=1
#--------------------------------------#

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1
#---------------------------------------#

nums = (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0
while i < len(nums):
    if (nums[i] == x):
        print("Found at idx", i)
    i +=1

#---------------------------------------#
i = 1
while i <= 5:
    if(i == 3):
        break
    i+=1