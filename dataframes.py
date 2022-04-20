#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydataset import data

data(show_doc=True)


# ### 1.  Copy the code from the lesson to create a dataframe full of student grades.
# 

# In[2]:


import pandas as pd
import numpy as np
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


# - a.  Create a column named passing_english that indicates whether each student has a passing grade in english.
# 

# In[3]:


df.english > 70
df['passing_english'] = df.english > 70

df


# - b. Sort the english grades by the passing_english column. How are duplicates handled?

# In[4]:


df.sort_values(by='passing_english')
# Sorted by False first then True based on their 0 & 1 values then by their index number


# - c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
# 

# In[5]:


df.sort_values(by='name').sort_values(by='passing_english')
# Rev recommended to sort it as a list instead of chaining.  df = df.sort_values(by=['passing_english', 'name'])


# - d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

# In[6]:


df.sort_values(by='english', ascending = False).sort_values(by='passing_english')
# Rev df = df.sort_values(by=['passing_english', 'english'], ascending=[False, False])
# Rev alt ans w/ single False. df = df.sort_values(by=['passing_english', 'english'], ascending=[False])


# - e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

# In[7]:


df['overall_grade'] = ((df.english + df.reading + df.math)/3)
df


# In[33]:


# to count the number of columns non-manually
df["over_all"] = df[["math", "english", "reading"]].mean(axis=1)
# applies the mean function to each row with axis=1
df.head()


# In[34]:


# hey boolean column, sum up your Trues
df.passing_english.sum()


# In[35]:


# mean gives us a proportion of trues from a boolean column
df.passing_english.mean()


# ### 2.  Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
# 

# In[9]:


data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable


# - How many rows and columns are there?

# In[10]:


mpg.shape
# 234 rows and 11 columns
# Rev you can access tuples using bracks like you do with lists using brackets []


# - What are the data types of each column?

# In[11]:


# the columns names are the index, "manufacturer", "model", "displ", "year", "cyl", "trans", "drv", "cty", "hwy", "fl"
mpg


# - Summarize the dataframe with .info and .describe

# In[12]:


print(mpg.info)
mpg.describe


# - Rename the cty column to city.

# In[13]:


print(mpg.rename(columns={'cty': 'city'}))

# Rev Make the chang to the original dataframe using inplace
# mpg.rename(columns = {'cty': 'city'}, inplace=True)


# - Rename the hwy column to highway.

# In[14]:


print(mpg.rename(columns={'hwy': 'highway'}))


# In[ ]:





# - Do any cars have better city mileage than highway mileage?

# In[15]:


mpg.cty > mpg.hwy
mpg['better_city_mileage'] = mpg.cty > mpg.hwy
mpg.sort_values(by='better_city_mileage')

mpg
# No, there's no city mileage better than highway mileage


# - Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
# 

# In[16]:


mpg['mileage_difference'] = (mpg.cty - mpg.hwy)
mpg


# - Which car (or cars) has the highest mileage difference?
# 

# In[36]:


mpg.sort_values("mileage_difference")
# volkswagen and honda are tied for the highest mileage difference at -12

# Rev mpg.mileage_difference == mpg.mileage_difference.max()
# mpg[mpg.mileage_difference == mpg.mileage_difference.max()]


# - Which compact class car has the lowest highway mileage? The best?
# 

# In[18]:


mpg.loc[mpg['class'] == 'compact'].sort_values(by='hwy')
# the volkswagen jetta has the lowest highway mileage

# Rev class is a reserved word, so if you use [] around 'class it will specify that column'
# mpg_compact[mpg_compac.highway == mpg_compact.highway.min()]


# - Create a column named average_mileage that is the mean of the city and highway mileage.
# 

# In[19]:


average_mileage = ((mpg.cty + mpg.hwy)/2)
print(average_mileage)
mpg['average_mileage'] = ((mpg.cty + mpg.hwy)/2)

mpg


# - How many rows and columns are there?
# 

# In[20]:


#234 rows x 14 columns


# - Which dodge car has the best average mileage? The worst?
# 

# In[21]:


mpg.loc[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage', ascending=False).head()
# The caravan 2wd has the best average mileage for a dodge


# ### Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# In[22]:


data('Mammals', show_doc=True) # view the documentation for the dataset
Mammals = data('Mammals') # load the dataset and store it in a variable


# - What are the data types?

# In[23]:


Mammals.dtypes
# The data types for mammals are float64


# In[24]:


Mammals


# - Summarize the dataframe with .info and .describe
# 

# In[25]:


print(Mammals.info)
Mammals.describe


# - What is the the weight of the fastest animal?
# 

# In[26]:


Mammals.sort_values(by='speed', ascending=False).head(1)
# The weight of the fastest animal is 55.0 kg

# Rev df[df.speed == df.speed.max()]


# - What is the overal percentage of specials?
# 

# In[27]:


print(Mammals.shape)
print(Mammals.shape[0])
print(Mammals[Mammals.specials == True])
print(Mammals[Mammals.specials == True].shape)
print(Mammals[Mammals.specials == True].shape[0])
print((Mammals[Mammals.specials == True].shape[0]/Mammals.shape[0])*100, '%')

# Rev df.specials.sum() / len(df)
# df.specials.mean()


# - How many animals are hoppers that are above the median speed? What percentage is this?
# 

# In[28]:


# Total speed of all animals
print(Mammals.speed.sum())
# Total number of animals
print(Mammals.shape[0])
# Mean speed calc'd by dividing the total speed by the number of animals
print((Mammals.speed.sum())/(Mammals.shape[0]))
# Boolean result for all animals faster than the mean speed
print(Mammals.speed > (Mammals.speed.sum())/(Mammals.shape[0]))
# List of all animals whose speed is greater than the mean speed
print(Mammals[Mammals.speed > (Mammals.speed.sum())/(Mammals.shape[0])])
# Shows boolean info for hoppers column of animals whose speed is greater than the mean
print(Mammals.hoppers[Mammals.speed > (Mammals.speed.sum())/(Mammals.shape[0])])
# Lists hoppers above mean speed by combining boolean statements requiring it to be a hopper & also above the mean speed
print(Mammals[(Mammals.hoppers == True) & (Mammals.speed > (Mammals.speed.sum())/(Mammals.shape[0]))])
# Grabs the shape of the above dataset
print(Mammals[(Mammals.hoppers == True) & (Mammals.speed > (Mammals.speed.sum())/(Mammals.shape[0]))].shape)
# Gets the total rows of the shape of the dataset
print(Mammals[(Mammals.hoppers == True) & (Mammals.speed > (Mammals.speed.sum())/(Mammals.shape[0]))].shape[0])
# Uses the number of rows and divides by total number of original dataset then multiplies it by 100 to get the percentage
print((Mammals[(Mammals.hoppers == True) & (Mammals.speed > (Mammals.speed.sum())/(Mammals.shape[0]))].shape[0]/Mammals.shape[0])*100, '%')



# There's 7 hoppers above the mean speed making up 6.5420560747663545% of total animals

# Rev df[(df.hoppers == True) & (df.speed > df.speed.median())]
# fast_hoppers = df[(df.hoppers == True) & (df.speed > df.speed.median())]
# Use len(df) to get the number of rows


# In[29]:


# Awesome Bonus

# For much more practice with pandas, Go to https://github.com/guipsamora/pandas_exercises and clone the repo down to your laptop. To clone a repository: - Copy the SSH address of the repository - cd ~/codeup-data-science - Then type git clone git@github.com:guipsamora/pandas_exercises.git - Now do cd pandas_exercises on your terminal. - Type git remote remove origin, so you won't accidentally try to push your work to guipsamora's repo.

# Congratulations! You have cloned guipsamora's pandas exercises to your computer. Now you need to make a new, blank, repository on GitHub.

# Go to https://github.com/new to make a new repo. Name it pandas_exercises.
# DO NOT check any check boxes. We need a blank, empty repo.
# Finally, follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.
# Now do your own work, add it, commit it, and push it!

