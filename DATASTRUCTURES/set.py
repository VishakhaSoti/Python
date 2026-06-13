set1 = {54, 67, 24,10,96}
print(set1)

set2 = {}    #set without any object/dat is a dictionary.

set3 = {2,55,7,29,80}
set3.add(64)
set3.update([55,77])
print(set3)

fruits = {"apple", "banana", "orange"}
new_fruits = {"mango", "kiwi", "cherry"}
fruits.update(new_fruits)
print(fruits)

set4 = {'a','v','c','m','o'}
set5 = {'a','e','i','o','u'}
new = set4-set5
new1= set4|set5           #prints all the values
new2= set4 & set5         #prints the common values
new3= set4 ^ set5         #prints the non-common values
print(new)
print(new1)  
print(new2) 
print(new3)

#QUESTION

a = set('telusko')
b = set('python')
print(a&b)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a&b)