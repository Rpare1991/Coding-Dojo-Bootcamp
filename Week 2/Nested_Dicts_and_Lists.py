# *** NOTE: I suggest running each code block seperately as some variable names are reused. ***

# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]
#------------------------------------------------------------------------#
# 2. Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of 
# dictionaries, the function loops through each dictionary in the list and
#  prints each key and the associated value. 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for x in range(len(students)):
        print("first_name - " + students[x]["first_name"] + ", last_name - " + students[x]["last_name"] )
        
    return

iterateDictionary(students)
#------------------------------------------------------------------------#
# 3.Get Values From a List of Dictionaries 
# Create a function iterateDictionary2(key_name, some_list) that, given a
# list of dictionaries and a key name, the function prints the value stored 
# in that key for each dictionary.
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, students):
     for x in range(len(students)):
        print(students[x][key_name])
       
            

iterateDictionary2("last_name",students)

#------------------------------------------------------------------------#
#Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values
# are all lists, prints the name of each key along with the size of its list,
# and then prints the associated values within each key's list. 

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key, value in dojo.items():
        print(str(len(value)) + " " + key)
        for x in range(len(value)):
                print(value[x])
        print("")

printInfo(dojo)
