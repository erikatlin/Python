#!/usr/bin/env python
# coding: utf-8

# <b> Create two dictionaries: PersonalInfo with 13 key-value pairs & WorkInfo with 7 key-value pairs. <b>

# In[1]:


PersonalInfo = {"a":"apple","b":"banana","c":"corn","d":"dog","e":"egg","f":"flan","g":"goat",
               "h":"ham","i":"ice","j":"juice","k":"kale","l":"lamb","m":"meat"}
print(PersonalInfo)


# In[2]:


WorkInfo = {"n":"naan","o":"octopus","p":"pizza","q":"quinoa","r":"rice","s":"steak","t":"tea"}
print(WorkInfo)


# <b> Add two new pairs key-value to the dictionary PersonalInfo and remove three key-value pairs from WorkInfo. Print results after the 2 operations <b>

# In[3]:


PersonalInfo["u"] = "ube"
PersonalInfo["v"] = "veal"
print(PersonalInfo)


# In[4]:


del WorkInfo ["n"]
del WorkInfo ["o"]
del WorkInfo ["p"]
print(WorkInfo)


# <b> Concatenate the 2 dictionaries and print all 3 dictionaries. Iterate through the compound dictionary by printing every key-value pair, each on one line. <b>

# In[5]:


PersonalInfo.update(WorkInfo)
print(PersonalInfo)

for k, v in PersonalInfo.items():
    print(k,"-->",v)


# <b> Sort the compound dictionary by keys in descending order and print one record per line. <b>

# In[6]:


sorted_keys = sorted(PersonalInfo, key = PersonalInfo.get, reverse = True) 
for key in sorted_keys:
    print(key)


# In[ ]:




