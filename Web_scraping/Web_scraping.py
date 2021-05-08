#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
import requests
from bs4 import BeautifulSoup


# In[23]:




URL = 'https://twitter.com/LoganPaul/status/1390342858805321734'
page = requests.get(URL).text

soup = BeautifulSoup(page, 'lxml')
results = soup.find_all('div',class_c='css-1dbjc4n')
print(results)


# In[ ]:





# In[ ]:


pd
L=df.values.tolist()

with open('my_scraped_data.csv','w',newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow('txt')
    for i in L:
        thewriter.writerow([i])


# In[ ]:




