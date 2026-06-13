dict1 = {'a':1, 'b': 2, 'c': 3, 'd': 4}
print(dict1['d'])
print(dict1.get('b'))

print(dict1.get('t', 'not found'))

#dict is a collection of key and values
#key:value, set:list
#set cannot repeat values, but list can

keys = {'tashu', 'ayush', 'aditi'}
values = {23, 26, 29}
dict2 = dict(zip(keys, values))          #will not give output in the same order
print(dict2)

#QUESTION

data = {
    "harsh": ['java','python','ai'],       #set, we can change values
    "navin": {'frontend': 'react', 'backend': 'spring'},      #dict within a dict
    "kiran": ('js', 'flask')     #tuple, we cannot change values
}

print(data["navin"]['backend'])
#-------------------------------------------------------------------------------------#

student = {
    "name" : 'Vishakha',
    "marks" : {
        "eng": 44,
        "math": 55
    },
    "grade": "A"
}

pairs = list(student.items())
print("1)", pairs[0])
print("2)",pairs[1])
print("3)",pairs[2])