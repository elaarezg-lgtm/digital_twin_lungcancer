#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install pandas matplotlib seaborn openpyxl requests')


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df = pd.read_csv("mutations.csv")

df.head()


# In[10]:


import os
os.getcwd()


# In[11]:


os.listdir()


# In[12]:


df = pd.read_csv("mutations.csv")

df.head()


# In[13]:


egfr_df = df[df["hugoGeneSymbol"] == "EGFR"]

egfr_df.head()


# In[14]:


mutation_counts = egfr_df["proteinChange"].value_counts()

mutation_counts.head(10)


# In[15]:


import pandas as pd

df = pd.read_csv("mutations.csv", sep=";")

df.head()


# In[16]:


df.columns


# In[17]:


mutation_counts = df["proteinChange"].value_counts()

mutation_counts.head(10)


# In[18]:


import matplotlib.pyplot as plt

mutation_counts.head(10).plot(kind="bar")

plt.title("Top EGFR Mutations")
plt.xlabel("Mutation")
plt.ylabel("Frequency")

plt.show()


# In[19]:


top_mutations = mutation_counts.head(10)

top_mutations


# In[20]:


df["isHotspot"].value_counts()


# In[21]:


hotspots = df[df["isHotspot"] == True]

hotspots["proteinChange"].value_counts().head(10)


# In[22]:


import matplotlib.pyplot as plt

plt.hist(df["proteinPosStart"], bins=50)

plt.title("Distribution of EGFR mutation positions")
plt.xlabel("Protein position")
plt.ylabel("Mutation count")

plt.show()


# In[23]:


import seaborn as sns

top10 = df["proteinChange"].value_counts().head(10)

sns.barplot(x=top10.values, y=top10.index)

plt.title("Top EGFR Mutations in Dataset")
plt.xlabel("Frequency")
plt.ylabel("Mutation")

plt.show()


# In[ ]:




