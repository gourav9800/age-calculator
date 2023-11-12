#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
year=int(input())
month= int(input())
date=int(input())
hours=int(input())
minutes=int(input())
secounds=int(input())
x=datetime.datetime.now()
y=datetime.datetime(year,month,date, hours,minutes, secounds)
age=x-y
years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30
remaining_days = remaining_days - (months * 30)
days = remaining_days
age_text = "You are " + str(years) + " years, " + str(months) + " months, " + str(days) + " days"
print(age_text)


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




