#!/usr/bin/env python
# coding: utf-8

# <b> Strings, List, Tuples <b>

# In[2]:


#Code prompts written by Cris Doloc
#Code responses written by Erika Lin


# <b> Transform the input string such that you will create another string by removing the characters of odd index values and replace them with the first character of the input string. Print the modified string! <b>

# In[11]:


unreplaced_string = input()

def remove_odd_characters(unreplaced_string):
    x = 0 #set the x variable to the first index value of 0
    replaced_string = "" #the contents of the for loop should loop into this variable
    for char in unreplaced_string:
        original_character = unreplaced_string[0] #the index value position will start at 0 and continue to loop 
        if (x %2 == 0): #if the index value is even
            replaced_string += unreplaced_string[x]
        elif (x %2 !=0): #if the index value is odd
            replaced_string += original_character #at an odd index value: keep the original character 
        x +=1 #this tells x to keep adding 1 under the for loop until the end of the input()
            
    return replaced_string
        
    print(replaced_string)

remove_odd_characters(unreplaced_string)


# <b>  Reverse the string obtained above by using three different implementations. Print the new string! <b>

# In[12]:


####Method 1 

unreplaced_string[::-1]


# In[13]:


####Method 2
def reversed_string(unreplaced_string):
    pos_last_char = (len(unreplaced_string) - 1) #position of the last character is the total length of the word subtracted from 1 
    #since index values start at 0 we want the position to start at one less value to start at index value 0
    n = pos_last_char #set the n variable to the pos_last_char variable for simplification purposes
    reverse_char = "" #the contents of the for loop should loop into this variable 
    for char in unreplaced_string:
        reverse_char += unreplaced_string[n] #reverse_char is itself added to the character at the position value of n
        #n should start at 0 and continue to print until the end of the word
        n = n - 1 #put n inside for loop or else it will print 'ooooo' and tell n to subtract by one to reverse the string from 
        #index values will go from 0,-1,-2,...
        

    return reverse_char
    print(reverse_char)

reversed_string(unreplaced_string)


# In[14]:


####Method 3

def reversed_string(unreplaced_string):
    if unreplaced_string == "":
        return unreplaced_string
    else: 
        return reversed_string(unreplaced_string[1:])+unreplaced_string[0]
    
reversed_string(unreplaced_string)


# <b> Write a Py function that takes the numerical list from the input and returns another list from where the largest and smallest elements were replaced by 1000, respectively -1000. Print the new list! <b>

# In[16]:


s = input("Introduce a list with numbers: ")
myList = list(map(int, s.split())) #do not include commas

def max_min_in_list(myList):
    n = 0
    my_max = myList[n]
    my_min = myList[n]
    for char in myList:  
        if char > my_max: #my_max is looping at index values n
            my_max = char
        elif char < my_min:#my_min is looping at index values n
            my_min = char
        n = n + 1  #tells n to continue counting by 1 until the end
    myList.remove(my_max) 
    myList.remove(my_min)
    
    myList.insert(my_max,"1000") 
    myList.insert(my_min, "-1000")
    
   
    return myList


    print(myList)

max_min_in_list(myList)


# <b> Sort the elements of a tuple in a decreasing order. <b>

# In[17]:


s = input("Introduce a tuple: ")
my_tuple = tuple(map(int, s.split()))

tuple_to_list = list(my_tuple) 
new_list_from_tuple = sorted(tuple_to_list)#sorted will make it from smallest to biggest # 
decreasing_tuple = new_list_from_tuple[::-1]
new_tuple = tuple(decreasing_tuple)

print(new_tuple)
type(my_tuple)
print(type(my_tuple))


# In[ ]:




