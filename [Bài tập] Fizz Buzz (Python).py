#!/usr/bin/env python
# coding: utf-8

# In[9]:


n=input("nhap: ")
batdau = int(n[0])
ketthuc=int(n[-1])
if ketthuc<batdau:
    print("ketthuc phai lon hon batdau")
else:
    for i in range (batdau):
        if i%3==0 and i%5==0:
            print("FIZZBUZZ")
        elif i%3==0:
            print("FIZZ")
        elif i%5==0:
            print("BUZZ")   
        else:
            print(i)


# In[ ]:





# In[ ]:




