f = open("textfile.txt", "r")                  #READ MODE
data = f.read()
print(data)
# print(type(data))
f.close()
#-----------------------------------#
f = open("textfile.txt", "r")
line1 = f.readline()
print(line1)                #LINE1
line2 = f.readline()
print(line2)                #LINE2
line3 = f.readline()
print(line3)                #LINE3
f.close()
#-----------------------------------#
f = open("textfile.txt", "r+")        #OVERWRITES FROM THE BEGINNING 
f.write("abc")
f.close()