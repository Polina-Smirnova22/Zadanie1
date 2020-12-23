#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = list (input ("number = "))
if a.count ('6') > 0:
    a.insert(a.index('6'), '9')
    a.remove ('6')
print ("".join(str(i) for i in a))


# In[ ]:




