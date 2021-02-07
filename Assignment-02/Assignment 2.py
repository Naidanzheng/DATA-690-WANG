#!/usr/bin/env python
# coding: utf-8

# # Assignment 2:

# 1. Prompts a user to enter 10 integers.
# 2. If the user enters anything other than integers, remind her that only integers are allowed and let her retry.
# 
# Note: You need to detect if use makes a mistake and let the user retry without exiting the program. The previously entered valid inputs should be kept and not lost.
# Don't allow the user to enter more than 10 or less than 10 integers.
# 3. Display the 10 integers back to the user at the end.
# 4. Calculate the following statistics from the 10 integers entered and display the results back to the user:
#    Minimum
#    Maximum
#    Range
#    Mean
#    Variance
#    Standard Deviation

# In[27]:


numbers = [] #create empty list

while len(numbers) < 10:  #length of the list should be less than 10.

    num = input(f"\nPlease enter an integer: ")

    try:
        num = int(num)
        numbers.append(num)
    except:
        print("\nInvalid. Please enter an integer.")

print("\n", numbers)  #The numbers that entered.


# In[28]:


total = 0
for num in numbers:
    total += num

print(f"Sum is:", sum(numbers))  # The sum of the list
print(f"Average number = {total/len(numbers)}" ) # The average number of the list
print(f"Minimum number is:", min(numbers))   #The minimum number of the list
print(f"Maximum number is:", max(numbers))   #The maximum number of the list
print(f"Range number is" ,(max(numbers))- min(numbers))  #The range number of the list


# In[29]:


def variance(numbers): # Calculate the variance of the list.
   
  n = len(numbers)
   
  mean = sum(numbers) / n
   
  deviations = [(x - mean) ** 2 for x in numbers]
    
  variance = sum(deviations) / n
  return variance


# In[30]:


def stdev(numbers): # Calculate the standard deviation of the list
  import math
  var = variance(numbers)
  std_dev = math.sqrt(var)
  return std_dev


# In[31]:


print("Standard Deviation of the list is % s "% (stdev(numbers)))
print("Variance of the list is % s "% (variance(numbers)))

