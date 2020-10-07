#!/usr/bin/env python
# coding: utf-8

# # Sorting & Searching
# ## I. Sorting
# ## Fungsi Swap

# In[4]:


#swap function
var1 = 1
var2 = 2
var1,var2 = var2,var1


# In[5]:


print(var1,var2)


# ## 1. Bubble Sort

# In[6]:


list = [34,43,23,12,54,17,46]
#modifikasi sesuai angka favorite anda


# In[7]:


#proses penukaran bubble sort

lastElementIndex = len(list)-1
print(0,list)
for idx in range(lastElementIndex):
    if list[idx]>list[idx+1]:
        list[idx],list[idx+1]=list[idx+1],list[idx]
    print(idx+1,list)


# In[8]:


list


# In[11]:


def BubbleSort(list):
    #Exchange the element to arrange in order
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
    return list


# In[14]:


list = [34,43,23,12,54,17,46]


# In[15]:


BubbleSort(list)


# In[16]:


list


# # 2. Insertion Sort

# In[17]:


def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]
        while (list[j] > next) and (j >= 0):
            list[j+1] = list[j]
            j=j-1
            list[j+1] = next
    return list


# In[18]:


list = [34,43,23,12,54,17,46]


# In[19]:


list


# In[20]:


InsertionSort(list)


# In[21]:


list


# # 3. Selection Sort

# In[25]:


def SelectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot],list[max_index] = list[max_index],list[fill_slot]
    return list


# In[26]:


list = [34,43,23,12,54,17,46]
SelectionSort(list)


# In[27]:


list


# ## II. Searching
# # SEARCHING ALGORITHMS
# ## 1. Linear Search

# In[29]:


def LinearSearch(list, item):
    index = 0
    found = False
    
# Match the value with each data element
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found


# In[30]:


list = [34,43,23,12,54,17,46]
print(LinearSearch(list,34))
print(LinearSearch(list,4))


# ## 2. Binary Search

# In[32]:


def BinarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False
    
    while first<=last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


# In[34]:


list = [34,43,23,12,54,17,46]
sorted_list = BubbleSort(list)
print(BinarySearch(list,34))
print(BinarySearch(list,4))


# # Interpolation Search

# In[35]:


def IntPolsearch(list,x ):
    idx0 = 0
    idxn = (len(list) - 1)
    found = False
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:

# Find the mid point
        mid = idx0 +int(((float(idxn - idx0)/(list[idxn] - list[idx0])) * ( x - list[idx0])))

    # Compare the value at mid point with search value
        if list[mid] == x:
            found = True
            return found
        
        if list[mid] < x:
            idx0 = mid + 1
    return found


# In[36]:


list = [34,43,23,12,54,17,46]
sorted_list = BubbleSort(list)
print(IntPolsearch(list,34))
print(IntPolsearch(list,4))


# # Testing Code di Video

# In[3]:


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)
    
from operator import attrgetter
    
e1= Employee('Carl', 37, 70000)
e2= Employee('Sarah', 29, 80000)
e3= Employee('John', 43, 90000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)


# In[ ]:




