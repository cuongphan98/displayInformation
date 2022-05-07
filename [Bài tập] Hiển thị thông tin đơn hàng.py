#!/usr/bin/env python
# coding: utf-8

# In[13]:


m = int(input("nhap so tien: "))
if m < 75:
    total = m
    print(total)
elif m >= 75 and m <100:
    total= m -15
    print(total)
elif m >= 100 and m < 150:
    total= m -25
    print(total)
else:
    total= m -50
    print(total)


# In[ ]:




