num = 2

if num==1:
    print("One")
elif num==2:
    print("Two")
elif num==3:
    print("Three")
elif num==4:
    print("Four")
elif num==5:
    print("Five")
else:
    print("Incorrect")

#------------------------#

score = 95

if score >= 90:
    print("Grade A+")
elif score >= 75:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")

#--------------------------#
#Traffic Light

light = input("Enter Light: ")

if (light == "red"):
    print("STOP")
elif (light == "yellow"):
    print("LOOK")
elif (light == "green"):
    print("GO!")
else:
    print("LIGHT IS BROKEN")