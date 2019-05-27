#!/usr/bin/env python
# coding: utf-8

# <b> Load data from the File-input.csv file into a pandas dataframe and print it to the Jupyter console. <b>

# In[12]:


import os


# In[4]:


import pandas as pd


# In[5]:


dataframe = pd.read_csv("File-input.csv")
dataframe


# <b> Convert the dataframe into a list of Dictionaries using the .to_dict method and then save all the records from the pandas dataframe as different dictionaries. Orient them as 'records' and print them on different lines. <b>

# In[6]:


result = dataframe.to_dict(orient = 'records')

for row in result:
    dict = row.copy()
    print(dict)


# <b> Access and print the 5th dictionary as 5th record of the pandas dataframe. <b>

# In[7]:


n = 4
print(result[n])


# <b> List all the keys of this dictionary, one per line, and then create a list with the them called “headers”. <b>

# In[8]:


dict = result[n]

for key in dict.keys():
    print(key)
print()

headers = list(dict.keys())
print(headers)


# <b>Select and print the 3rd element in the list. <b>

# In[9]:


n = 2
print(headers[n])


# <b> Modify the values for "Temp" and "Weight" keys for this specific record. <b>

# In[10]:


dict["Temp"] = 100.0
dict["Weight"] = 200
print(list(dict.values()))


# <b> Find the "Last name" that has the max value of "Weight" from the dataframe. <b>

# In[11]:


df = dataframe[['Last name','Weight']]
result = df.to_dict(orient='records')

max = -1
solution = ((),)
for row in result:
    weight = row['Weight']
    last_name = row['Last name']
    if weight > max:
        max = weight
        solution = last_name, weight
print(solution)


# In[ ]:




