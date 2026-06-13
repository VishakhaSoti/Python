num1 = [12,23,37,40,58,69]
print(num1[4])

num2 = [23, "tashu", 55.6]
print(num2[1][3])

num3 = [45,67,23,48]
name1 = ["tashu", "ayush", "nona"]
mix = [num3, name1]
print(mix)

num4 = [29,40, 29, 47, 62]
num4.pop(1)  #removes value with index no.#
num4.append(65)
print("the count of 29 is", num4.count(29))
print(num4)

a = [2,45,63,82]
print(63 in a)

list = [2,1,3]
list.sort()
print(list)

#QUESTION

a = [33,76,24,56]
b = ["navin", "kiran", "harsh"]
print((a[:2] + b[1:])[-3])