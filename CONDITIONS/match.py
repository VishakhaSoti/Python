num = 3

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Incorrect")

#------------------------------------#

num = 15
match num % 3:
    case 0:
        print("Divisible by 3")
    case 1:
        print("Remainder 1 when divided by 3")
    case _:
        print("Remainder 2 when divided by 3")

#-------------------------------------------------#