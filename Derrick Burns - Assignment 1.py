#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Nested conditional
# Derrick has class on Monday's at 9am and 6pm, Tuesday's & Thursday's at 3pm, and Wednesday's at 9am.
# He does not have class any other day or time of the week.
# Write a nested conditional to show his class schedule. Use a variable input variable for day and time.


day = input("Enter a day of the week: ")       # variable to input day of week as str
time = int(input("Enter a time 1-12: "))       # variable to input time of class as int
if day.lower() == "monday":          # if the day of the week entered equals Monday and time equals 9 or 6, Derrick has class
    if time == 9:                    # if not, he does't have class at that time of day
        print("I have ISM4930")
    elif time == 6:
        print("I have ISM4402")
    else:
        print("I don't have class")
        
elif day.lower() == "tuesday":                  # if the day of the week equals Tuesday and time equals 3
    if time == 3:                                  # Derrick has class, if not, he doesn't have class at that time of day
        print("I have ISM4300")
    else:
        print("I don't have class")
        
elif day.lower() == "wednesday":           # if the day of the week equals Wednesday and time equals 9, Derrick has class
    if time == 9:                          # if not, he doesn't have class at that time of day
        print("I have ISM4930")
    else:
        print("I don't have class")
        
elif day.lower() == "thursday":                    # if the day of the week equals Thursday and time equals 3
    if time == 3:                                  # Derrick has class, if not, he doesn't have class at that time of day
        print("I have ISM4300")
    else:
        print("I don't have class")
        
else:                                      # Derrick doesn't have class at all this day
    print("I don't have class at all")


# In[3]:


# Nested conditional #2
# Write a nested conditonal that tests if is x equal to y, and if that's false, another test for x is less than y.


x = int(input("Input x: "))          # variable x to input a number
y = int(input("Input y: "))          # variable y to input a number
if x == y:                           # if statement for x equal to y
    print(x, "and", y, "are equal")  # print result
else:
    if x < y:                       # if statement for x less than y
        print(x, "is less than", y) # print result
    else:
        print(x, "is greater than", y)   # print result for else if the if statement is false


# In[ ]:


# Iterative example (while loop)
# While x is less than 5 print x
# x will iterate until the statement is false.


x = 0;     # set up variable for x
while (x < 5):     # while loop stating x is less than 5
    print(x)     # print x
    x += 1     # x adds 1 each iteration


# In[10]:


# Iterative example (for loop)
# Define a list with these car brands: Honda, Toyota, Ford, Kia, Hyundai, and Nissan
# Print each element in the list

cars = ["Honda", "Toyota", "Ford", "Kia", "Hyundai", "Nissan"] # created list with variable cars
for i in cars:
    print(i)      # print i


# In[ ]:




