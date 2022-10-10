# NOTE: I suggest running each code block seperately as some variable names are reused.

# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).

def countdown(): #Function declaration

    print ('Please enter a starting number to count down from.') # asks for input from user
    num_max = int(input()) #Sets the value to count down from to user input
    num_list = []   # creates list to store values
    num_list.append(num_max) #set the first value to starting num

    for x in range(num_max): # loop that iterates through and counts down, adding the value to list
    
        num_max -= 1
        num_list.append(num_max)

    return num_list #Exit function and return list 
print(countdown()) # prints out to terminal by calling countdown function
#----------------------------------------------------------------------------------------------------------------------------------
#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(list): #Function declaration, accepts a list as a parameter
    
    print(list[0])  #Prints the first value in list
    return(list[1])  #Returns the second value in list

print_and_return([1,2]) #Calls function with list values
#----------------------------------------------------------------------------------------------------------------------------------
#First Plus Length- Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(list):  #Function declaration, accepts list as a parameter
    return list[0] + len(list)  #Sums the first value in list plus the length of the list.

first_plus_length([1,2]) #Calls function with list

#----------------------------------------------------------------------------------------------------------------------------------
#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original 
# list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 
# 2 elements, have the function return False

def greater_than_second(list): #Function declaration, accepts list as a parameter
    if len(list) < 2:   # Before running for loop, validate that the list is greater than 2, if not return false
        return False
    new_list =[]   #declare new list variable
    

    for x in range(len(list)):      # interate through list and verify if the current index is greater than 2nd value
        if list[x] > list[1]:
            new_list.append(list[x])        #If index is greater than 2nd value, add to new list
            
        
   
    print(len(new_list))      # prints the amount of values in new list and returns new list
    return(new_list)


greater_than_second([5,2,3,2,1,4])
greater_than_second([3])

#----------------------------------------------------------------------------------------------------------------------------------
#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and 
# return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size, value):  # Function declaration, accepts size of list and repeated value as paramaters
    list = []       #  list declaration
    for x in range(size):  #For loop that continues until reaching size, adds value to list after each iteration
        list.append(value)
        x += 1
    return list

length_and_value(6, 2)
length_and_value(4, 7)