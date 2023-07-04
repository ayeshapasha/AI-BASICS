#!/usr/bin/env python
# coding: utf-8

# # <center>  (AI)
# Total Points: 50

# In[6]:


Your_Name = "Ayesha Fathima"
Your_Email_id = "ayeshapasha20@gmail.com"


# In[5]:


# imports and setup

# linear algebra
import numpy as np

# plotting graphs
import matplotlib.pyplot as plt 


# ### Q1 (2 points)
# Which of the following statements is used to terminate the statement ?
# 
# > A. Next
#  
# > B. Switch
# 
# > C. Break
# 
# > D. With
# 

# In[4]:


# print your answer. for ex if your answer is B
# print("B")

print("C")


# ### Q2 (2 points)
# For the below code, specify the datatype of variable X,
# 
# X = 'achgd7698'
# 
# > A. Complex 
# 
# > B. String 
# 
# > C. Integer
# 
# > D. Boolean
# 

# In[5]:


# print your answer.
print("B")


# ### Q3 (2 points)
# Consider the if-elseif-else statement, how many elseif are possible between if and else statements?
# 
# > A. 1
# 
# > B. 0
# 
# > C. Multiple
# 
# > D. None of the above
# 

# In[6]:


# print your answer.

print("C")


# ### Q4 (2 points)
# What will be the data type of variable 'C' after executing this code ?
# 
# A = 5
# 
# B = 6
# 
# C = print(A/B)
#  
# > A. Float
# 
# > B. None-type
# 
# > C. Int
# 
# > D. Object
# 

# In[17]:


# print your answer.

print("A")


# ### Q5 (5 points)
# Write a function that takes any number N as input and returns the square of that number.

# In[9]:


# complete the code below

def fibonacci(N):
    
    
    return N*N


N = int(input())

print("The square of N is: ", fibonacci(N))


# ### Q6 (8 points)
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[23]:


# write your solution here

x=[]
for n in range (2000,3201):
    
    if (n%7==0)and(n%5!=0):
        
        x.append(str(n))
        
        c=(','.join(x))
        
print (c)     
               


# ### Q7 (5 points)
# Write a Python program to accept the user's first and last name and then get them printed in the reverse order with a space between first name and last name.

# In[18]:


# write your code here

name = input()

print (name[::-1])


# ### Q8 (3 points)
# Given this given nested list, use indexing to grab and print the word "hello".
# 

# In[75]:


lst=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

# print the word 'hello' using list indexing 

print(lst[3][1][2])


# ### Q9 (3 points)
# Debug the following code. (We want to print the cube of third element of numpy array "a")
# 

# In[76]:


import numpy as np

a = np.array([1,2,3]) 


print (3*3*3)


# ### Q10 (5 points)
# Complete the following code. We want to plot a graph between "distance"(s) and "time" (t).
# 
# HINT: s = ut + 1/2 at2

# In[77]:


# complete the code below
import numpy as np
u = 10
a = 2

# use numpy to define an array t that will contain 100 elements 
# from 0 to 100 spaced evenly 
t = np.random.randint(0,100,2)

# use the formula defined above
s = (u*t)+(0.5*a*t*t)


# use plt to plot the graph
plt.plot(s,t)
plt.show()


# # Q11 (3 points)
# Which of the following statement is false?
# 
# > A. ndarray is also known as the axis array
# 
# > B. ndarray.dataitemSize is the buffer containing the actual elements of the array. 
# 
# > C. NumPy main object is the homogeneous multidimensional array
# 
# > D. In Numpy, dimensions are called axes

# In[78]:


# print your answer here

print("A")


# ### Q12 (5 points)
# 
# Share your views on the upcoming Moon Missions. Do you think ISRO will succed with Chandrayaan-3? (Explain in Atleast 100 words) 

# In[ ]:


# print your answer

my_answer = "Keeping in mind that Chandrayaan 2 was a almost a success with a minor failure indeed with the modifications made on Chandarayaan 3 such as not having an orbiter and including a lander and rover will demonstrate the soft landing with its four throttleable engines. Chandarayaan 3 will laso be accompanied with Laser Doppler Velocimeter which will help in the success of this mission."

print(my_answer)


# ### Q13 (5 points)
# 
# Describe your experience while learning python so far. Now that you are somewhat familiar with this tool, can you name some more use cases and examples where we can use python. (Atleast 150 words)

# In[24]:


# print your answer

my_answer = " Python is indeed a very usefool tool in this day and age, along with being useful it is also widely used in many aspects and places. With the advent of technology, programming languages are needed in every field and is of utmost importance for technological development. Python has many functions and is much easier to code in compared to other languages, these benefits make python one of the most popular languages in the world as of right now. There are many other languages that can also be used such as java and C programming which also have their own pros and cons.These coding languages such as python reduce burden and help with complex problems. Python can be used to code robots, for game development, for virtual reality, for software used for detection, for medical instrumentation using machine learning to increase accuracy, detecting illnesses with xray scans and other forms of images, etc."

print(my_answer)


# ### Q14 (Bonus)
# Tell us anything very interesting. And try asking a very intelligent question.

# In[26]:


# print your answer

my_answer = "In a parallel universe I am your teacher and you are my student. Space junk can be the cause for the end of the world if it keeps increasing, What is the best way to reduce space junk according to you?"

print(my_answer)


# ## Thank you for completing all the questions
# 
# 
# #### Download your notebook and submit it in the google form

# In[ ]:




