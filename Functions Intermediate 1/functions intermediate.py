#1   1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
from select import KQ_NOTE_RENAME


x = [ [5,2,3], [10,8,9] ] 

def changeX():
    x[1][0] = 15
changeX()
print(x)

#    2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def changeName():
    students[0]['last_name'] = 'Bryant'
changeName()
print(students)

#    3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def changeName():
    sports_directory['soccer'][0] = 'Andres'
changeName()
print(sports_directory)

#    4 Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

def changeValue():
    z[0]['y'] = 30
changeValue()
print(z) 



#2   Iterate Through a List of Dictionaries
#    Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and 
#     the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#def iterateDictionary(some_list):
#    for i in some_list:
#        for key in i.keys():
#            print(key + ' -')
#iterateDictionary(students)

def iterateDictionary(some_list):
    for items in some_list:
        for key in items:
            print(key, items[key])

iterateDictionary(students)



# bonus - With formatting to make it all on one line
def iterateDictionary(some_list):
    for items in some_list:
        one_line = ''
        for key in items:
            one_line += f'{key} - {items[key]}
            print(one_line)
iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3 #Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name,some_list):
    for some_dict in some_list:
        print(some_dict[key_name])

iterateDictionary2('first_name', students)








#4 Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key_name in some_dict:

        one_list = some_dict[key_name] 
        print(len(one_list), key_name.upper())

        for item in one_list:
            print(item)

        print("")

printInfo(dojo)