
# coding: utf-8

# In[75]:

from snownlp import SnowNLP
with open('D:/作业/NLP/chinese.txt') as f:
    c = f.read()
c


# In[76]:

s = SnowNLP(c)


# In[77]:

s


# In[78]:

paras = c.split('\n')
paras


# In[81]:

snows = [SnowNLP(para) for para in paras if not para.strip() == u'']
sents = [ snow.sentences for snow in snows]
sents


# In[83]:

sents[0]
sents[1]


# In[84]:

sents.__len__()


# In[86]:

snow = snows[0]
dir(snow)


# In[8]:

from numpy import *


# In[10]:

import numpy as np


# In[11]:

from numpy import array,sin


# In[12]:

a = [1,2,3,4]


# In[16]:

arr = array(a)


# In[17]:

a+1


# In[18]:

arr+1


# In[20]:

arr1 = array([6,7,8,9])
arr+arr1


# In[22]:

arr*arr1


# In[24]:

arr[0]


# In[26]:

arr[0:2]


# In[28]:

arr.shape


# In[29]:

arr.shape = 2,2


# In[31]:

arr


# In[32]:

import numpy as np


# In[33]:

import matplotlib.pyplot as plt


# In[35]:

linspace


# In[37]:

help(linspace)


# In[38]:

linspace(1,10,10)


# In[41]:

linspace(1,20,10)


# In[43]:

a = linspace(0,2*pi,21)
a


# In[ ]:

from numpy import sin


# In[45]:

x = linspace(0,2*pi,21)
y = sin(x)
y


# In[46]:

plt.plot(x,y)


# In[47]:

plt.show()


# In[49]:

x = linspace(0,10*pi,105)
y = cos(x)
plt.plot(x,y)
plt.show()


# In[51]:

help(plt.plot)


# In[52]:

plt.plot(x,y,'bo')
plt.show()


# In[60]:

plt.plot(y, 'ro')
plt.show()


# In[61]:

plt.plot(y, 'y*')
plt.show()


# In[66]:

from numpy import *
x = random.rand(200)


# In[67]:

x


# In[68]:

y = random.rand(200)
y


# In[70]:

size = random.rand(200)*30
color = random.rand(200)
plt.scatter(x,y,size,color)
plt.colorbar()
plt.show()


# In[ ]:




# In[ ]:



