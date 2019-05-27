#!/usr/bin/env python
# coding: utf-8

# <b> Create and print a numpy 1-d array containing 21 decimal numbers that starts at 5 and end at 10. Calculate and print the min, max and avarage value of this 1-d array. <b>

# In[1]:


import numpy as np


# In[2]:


my_array = np.linspace(5,10,21)
print(my_array)


# In[6]:


my_array.min(axis = 0)


# In[7]:


my_array.max(axis = 0)


# In[8]:


my_array.mean(axis=0)


# <b> Create and print a 2 dimensional array A that has 27 rows and 3 columns composed of consecutive integers. Change the shape of the array A to a new array B that has 9 rows and 9 columns and print it out. <b>

# In[9]:


A = np.arange(81).reshape(27,3)
print(A)


# In[10]:


B = np.arange(81).reshape(9,9)
print(B)


# <b> Add "elementwise" the numpy array obtained above (B) with the appropriate size identity array. Print the results. <b>

# In[11]:


identity = np.identity(9)
print(identity + B)


# <b>Multiply "dot-style" the numpy array obtained from summation with the array B and print the results.<b>

# In[12]:


dot_product = np.dot(identity,B)
print(dot_product)


# In[ ]:




