#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[10]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[11]:


df.hist()


# In[12]:


df.hist(column="Hours Worked", by="Gender")


# In[13]:


df.hist(column="Cars Sold", by="Gender")


# In[14]:


df.hist(column="Years Experience", by="Gender")


# In[17]:


df.boxplot(column="Hours Worked", by="Cars Sold")


# In[ ]:




