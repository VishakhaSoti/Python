f = open("textfile.txt", "w")                  #WRITE MODE (OVERWRITES THE TEXT)
data = f.write("Python is a coding language.")
print(data)
f.close()
#-----------------------------------------------------------------------------------------------------------------#
f = open("textfile.txt", "a")                 #APPEND MODE (ADDS TEXT IN  EXISTING DATA),(APPEND-ADD AT THE END)
data = f.write("Python is a coding language.")
print(data)
f.close()
#-----------------------------------------------------------------------------------------------------------------#

with open("practice.txt", "w") as f:                          #CREATING A PRACTICE.TXT FILE
    f.write("Hi everyone \nWe are learning file I/O \n")
    f.write("using Java. \nI like programming in Java.")
#-----------------------------------------------------------------------------------------------------------------#

with open("practice.txt", "r") as f:
    data = f.read()                               #REPLACES DATA
new_data = data.replace("Java","python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)                            #OVERWRITES DATA
#-----------------------------------------------------------------------------------------------------------------#

with open("practice.txt","r") as f:              #FINDING A WORD IN FILE
    data = f.read()
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("Not Found")
#-----------------------------------------------------------------------------------------------------------------#
 
def check_for_line():                           #FINDING THE LINE IN WHICH THE WORD EXIST
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()