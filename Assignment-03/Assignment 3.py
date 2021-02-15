#!/usr/bin/env python
# coding: utf-8

# #  Assignment 3    

# ### Problem 1: 

# In[22]:


import numpy #Import library

for i in range(10):                             
    matrix=numpy.random.randint(0,9,10)         
    print(*matrix)   


# ### Problem 2: 

# In[23]:


for i in range(10):                                           
    
    list_position=0          #set position
    matrix=numpy.random.randint(0,9,10).astype('object')      
                                                              
    for j in matrix:                                           
        list_position=list_position+1                         
        if j%2==1:                                            
            matrix[list_position-1]="@"  #replace it with @
    print(*matrix)       


# ### Problem 3: 

# In[24]:


for i in range(10):                         
    sum=0
    matrix=numpy.random.randint(0,9,10)      
    for number in matrix:                    
        sum=sum+number
    print(*matrix,end="")   
    print(" *",sum)         


# ### Problem 4:  Optional

# In[25]:


print("***********************")            

for i in range(10):                         
    matrix=numpy.random.randint(0,9,10)      
    print("* ",end="")                      
    print(*matrix,end="")                    
    print(" *")                             
print("***********************")            


# ### Problem 5:  Optional

# In[26]:


from numpy import random
a=[0,0,0,0,0,0,0,0,0,0]

for i in range(20):
    if i==10:
        for i in range(10):
            print("*   ",end='')
        print("\n")
        for i in range(10):
            print(a[i]," ",end='')
        break;
    sum1=0
    for j in range(10):
        b=random.randint(10)
        sum1+=b
        a[j]=a[j]+b
        print(b,"  ", end='')
    print("*", sum1,"\n")

