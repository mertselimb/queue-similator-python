#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[397]:


# 1 Line 4 ATM
def lines1atm4():
    newStudentTimer = 0
    serveTimer = [0,0,0,0]
    queue = 0
    servedStudent = 0
    for i in range(30000):
        # 4 atm
        for x in range(4):
            #Serve time
            if(serveTimer[x] == 0):
                if(queue != 0):
                    queue -= 1
                    serveTimer[x] = np.random.randint(15,180)
                    servedStudent += 1
            else:
                serveTimer[x] -= 1
                if(serveTimer[x] < 0):
                    serveTimer[x] = 0
        # new student
        if(newStudentTimer == 0):
            newStudentTimer = np.random.randint(5,40)
            queue += 1
        else:
            newStudentTimer -= 1
    print("(1 lines 4 atm) Served student number " + str(servedStudent))
    return servedStudent


# In[401]:


# 4 Lines 4 ATM

def lines4atm4():
    newStudentTimer = 0
    serveTimer = [0,0,0,0]
    queue = [0,0,0,0]
    servedStudent = 0
    for i in range(30000):
        # 4 atm
        for x in range(4):
            #Serve time
            if(serveTimer[x] == 0):
                if(queue[x] != 0):
                    queue[x] -= 1
                    serveTimer[x] = np.random.randint(15,180)
                    servedStudent += 1
            else:
                serveTimer[x] -= 1
                if(serveTimer[x] < 0):
                    serveTimer[x] = 0
        # new student
        if(newStudentTimer == 0):
            newStudentTimer = np.random.randint(5,40)
            index = 0
            small = 99
            for ix, val in enumerate(queue):
                if(small > val):
                    small = val
                    index = ix
            queue[index] += 1
        else:
            newStudentTimer -= 1
    print("(4 lines 4 atm) Served student number " + str(servedStudent))
    return servedStudent


# In[406]:


lines1atm4()


# In[408]:


lines4atm4()


# In[411]:


lines4arr = []
for _ in range(200):
    lines4arr.append(lines4atm4())
lines1arr = []
for _ in range(200):
    lines1arr.append(lines1atm4())


# In[412]:


print("4 lines 4 ATMs average : " + str(np.average(lines4arr)))
print("1 lines 4 ATMs average : " + str(np.average(lines1arr)))

