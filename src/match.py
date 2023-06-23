#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[6]:


def matching(tablet):
    choices = ['Dolo','Paracetamol','Soframycin','Crocin','Azithromycin','Disprin','Benadryl']

    ans = process.extractOne(tablet,choices)
    
    link = 'https://www.netmeds.com/catalogsearch/result?q={}'.format(ans[0])
    return ans[0], link


