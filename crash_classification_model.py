#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


# reading a csv file as dataframe

col_names = ['Township','Collision Date','Collision Time','Vehicles Involved','Number Injured','Number Dead','Light Condition','Weather Conditions','Surface Condition','Roadway Junction Type','Road Character','Roadway Surface','Primary Factor','Manner of Collision','Traffic Control']
df = pd.read_csv("crash-data-monroe-county-2019-3.csv", usecols=col_names)

display(df.head())
print(df.info())


# In[5]:


#Removing missing values

df=df.dropna()
display(df.head())
print(df.info())


# In[33]:


# A function to find the number of observations for unique value in a column of a DataFrame

def unique_val_count(data, column):
    df_count = df[column].value_counts()
    df_count = pd.DataFrame(df_count)
    df_count = df_count.reset_index()
    df_count = df_count.rename(columns={'index':column, column:'No of Accidents'})
    
    return df_count


# In[38]:



Surface_Condition_count = unique_val_count(df, 'Surface Condition')
Roadway_Junction_Type_count = unique_val_count(df, 'Roadway Junction Type')
Road_Character_count = unique_val_count(df, 'Road Character')
Roadway_Surface_count = unique_val_count(df, 'Roadway Surface')


# In[57]:


unique_val_count(df, 'Township')


# In[43]:


#Bar plot

# A function to show the number of observations for each unique value in a column using a barplot

def barplot(data, column_x, color, rotation, yticks):
    
    # create a barplot using seaborn
    sns.barplot(x=column_x, y='No of Accidents', data=data, color=color, alpha=0.75)
    
    # write a title for your plot
    plt.title("No of Accidents depending on " + column_x)
    
    # write proper lebel for the x and y axis
    plt.xlabel(column_x)
    plt.ylabel("No of Accidents")
    
    # rotate the xticks if necessary
    plt.xticks(rotation=rotation)
    
    # provide a range for the yticks
    plt.yticks(yticks)


# In[63]:


sns.set_context('paper')

plt.figure(figsize=(15,10))

# row 1, column 1
plt.subplot(2,2,1)
barplot(Surface_Condition_count, 'Surface Condition', 'blue', 90, np.arange(0,2800,200))

# row 1, column 2
plt.subplot(2,2,2)
barplot(Roadway_Junction_Type_count, 'Roadway Junction Type', 'orange', 90, np.arange(0,2200,200))

# row 2, column 1
plt.subplot(2,2,3)
barplot(Road_Character_count, 'Road Character', 'green', 0, np.arange(0,2200,200))

# row 2, column 2
plt.subplot(2,2,4)
barplot(Roadway_Surface_count, 'Roadway Surface', 'red', 0, np.arange(0,3500,200))

# write the title for all the plots
plt.suptitle("No of acciedents depending on various conditions")

# keep the individual plots separate from each other
plt.tight_layout()

# display the plots
plt.show()


# In[68]:


# Pie chart 
# A pie chart to show no of accidents depending on light conditions

df['Light Condition'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=180)

plt.xlabel("No of Accidents Depending on Light Conditions")
plt.ylabel("")
plt.show()


# In[89]:


sns.set_context('paper')
plt.figure(figsize=(8,6))
sns.scatterplot(x='Vehicles Involved', y='Number Injured', data=df)

plt.show()


# In[88]:


# number of unique values and their count in the 'Number Injured' column

df['Number Injured'].value_counts()


# In[70]:


# To determine whether there is injured or uninjured people in an accident

def check(x):
    if x>0:
        return 1
    else:
        return 0


# In[72]:


df['Injured'] = df['Number Injured'].apply(check)
display(df.head(5))


# In[73]:


# To indentify if anyone dead in an accident
def check(x):
    if x>0:
        return 1
    else:
        return 0
df['Dead'] = df['Number Dead'].apply(check)
display(df.head(5))


# In[74]:


# Classifying according to the severity of the accident
def check(df):
    if df['Injured']==0:
        if df['Dead']==0:
            return 0
        else:
            return 0.5
    else:
        if df['Dead']==0:
            return 0.5
        else:
            return 1
df['Severity']=df.apply(check, axis=1)
   
display(df.head(10))


# In[ ]:




