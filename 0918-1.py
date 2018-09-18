
# coding: utf-8

# In[1]:

from nltk.tokenize import sent_tokenize


# In[3]:

para = "hello world. it's good to see you.thanky you for buying this book."
sent_tokenize(para)


# In[5]:

from nltk.tokenize import word_tokenize
word_tokenize(para)


# In[13]:

from nltk import pos_tag


# In[14]:

pos_tag(word_tokenize(para))


# In[15]:

pos_tag(word_tokenize(para))

