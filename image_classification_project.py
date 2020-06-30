#!/usr/bin/env python
# coding: utf-8

# In[3]:


# importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


# using pandas to read the database stored in the same folder
data = pd.read_csv('mnist_test.csv')


# In[6]:


# viewing column heads
data.head()


# In[12]:


# extracting data from the dataset and viewing them up close
a = data.iloc[3,1:].values


# In[14]:


# reshaping the extracted data into a resonable size
a = a.reshape(28, 28).astype('uint8')
plt.imshow(a)


# In[15]:


# preparing the data
# separating labels and data values
df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]


# In[16]:


# creating test and train sizes/batches
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state=4)


# In[18]:


# check data
y_train.head()


# In[19]:


# call rf classifier
rf = RandomForestClassifier(n_estimators=100)


# In[20]:


# fit the model
rf.fit(x_train, y_train)


# In[21]:


# predicting on test data
pred = rf.predict(x_test)


# In[22]:


pred


# In[29]:


# check prediction accuracy
s = y_test.values

# calculate number of correct predicted values
count = 0
for i in range(len(pred)):
    if pred[i] == s[i]:
        count= count+1


# In[30]:


count


# In[31]:


# total values the the prediction code was run on
len(pred)


# In[32]:


# accuracy value
1889/2000


# In[ ]:




