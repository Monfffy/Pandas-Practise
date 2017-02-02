
# coding: utf-8

# ### An exercise in cleaning data with Pandas
# 
# #### You name: Mengfei Hu
# #### Your andrew ID: mengfeih

# Both Tue/Thu and Fri sections due:  2pm, Tuesday Jan 31 via Canvas.  
# 
# Treat this as a take home quiz: you are welcome to pose general questions on piazza;  your work needs to be independently done (without assistance from others or the TAs).  
# 
# This is a real formating problem I had to deal with once.  I'm using it as a simple exercise in pandas.
# 
# Based on what we've discussed this past week, I estimate it may take about an hour max.  This exercise will be graded with the below rubric:
# 
# - 2  : well done!  All requirements met
# - 1  : mostly correct
# - 0  : NB error, much remains to be done
# 
# We'll discuss the solution in class; hence no flex days can be applied.
# 
# ---
# 
# Examine the file `times.txt` in a text editor. I have provided segments from my NB that shows how the data frame is when initially read in and what the final form should be.
# 
# In this exercise you will
# 
# 1.  Read the data into a dataframe.  [Explore options for `read_table` that will read the data in the format shown below.].
# 
# 2. Set column and row labels as shown further down in the NB
# 
# 3. Adjust the index as shown
# 
# 4. Create two additional columns `s_dt` and `e_dt` that represent `datetime` versions of the string data in `start` and `end`.
# 
# 5. Finally calculate the difference between the values in the `e_dt` column and the `s_dt` column
# 
# Your final data frame should appear as shown in the very end of this notebook
# 

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_table('times.txt', sep='\s+', engine='python',skiprows=3,skipfooter=0,names=[0,1,2,3,4,5])
df.head()


# In[3]:

df.dtypes


# In[4]:

df = df.set_index(1)
df = df.set_index(df.index.str[0:3])
df.drop(4,axis=1,inplace=True)
#df.head()


# In[5]:

df.columns = ['day','dow','start','end']
df['dow'] = df['dow'].str[1:4]
#df.head()


# In[8]:

# You need to figure out how to convert a pandas columns of strings into
# Python 'datetime' objects. You will then store these converted values
# in a temporate column as show below.

df['s_dt']= pd.to_datetime(df['start'])
df['e_dt']= pd.to_datetime(df['end'])
df.head()


# In[9]:

df.dtypes


# In[10]:

# Finally calculate the differences between the e_dt and s_dt columns

#pd.to_timedelta(df['e_dt'] - df['s_dt'])
df['diff']=pd.to_timedelta(df['e_dt'] - df['s_dt'])
df.head()


# In[11]:

df.dtypes


# In[ ]:



