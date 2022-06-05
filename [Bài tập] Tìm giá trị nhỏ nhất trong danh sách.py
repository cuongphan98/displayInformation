#!/usr/bin/env python
# coding: utf-8

# In[6]:


number="123456789"
rs=""
min=9
for i in range(len(number)):
    if int(number[i]) < min:
        min=int(number[i])
        print(min)
rs+=min


# In[ ]:




