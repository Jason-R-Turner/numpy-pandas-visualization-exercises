#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import math as math
plt.figure(figsize=(14, 6)) # (width, height)

# 5. Make a new Jupyter notebook named big_o_notation.ipynb
# • Title your chart "Big O Notation"
# • Label your x axis "Elements"
# • Label your y axis "Operations"
# • Label your curves or make a legend for the curves
# • Use LaTex notation where possible


plt.title('$Big O Notation$')
plt.xlabel('$Elements$')
plt.ylabel('$Operations$')
# • y = 0n + 1 and label the curve "O(1)"

x = list(range(20, 81, 5))
y = [0*n + 1 for n in x]


plt.plot(x, y)
plt.annotate('$O(1)$', xy=(50, 0), xytext=(40, 10), arrowprops={'facecolor': 'blue'})


# • y = log(n) and label the curve "O(log n)"
y = [math.log(n) for n in x]
plt.plot(x, y)
plt.annotate('$O(log n)$', xy=(50, 50), xytext=(60, 10), arrowprops={'facecolor': 'yellow'})


# • y = n and label the curve "O(n)"
y = [n for n in x]
plt.plot(x, y)
plt.annotate('$O(n)$', xy=(35, 125), xytext=(25, 150), arrowprops={'facecolor': 'green'})

# • y = n∗log(n) and label it "O(n log n)"

y = [n * math.log(n) for n in x]
plt.plot(x, y)
plt.annotate('$O(n log n)$', xy=(20, 2.99), xytext=(23, 50), arrowprops={'facecolor': 'red'})


# plt.legend(loc='upper right')
# plt.title('Big O Notation')
# plt.xlabel('Elements')
# plt.ylabel('Operations')

# Curves to graph

# • y = n**2 and label it "O(n^2)"
y = [n**2 for n in x]
plt.plot(x, y)
plt.annotate('$O(n^2)$', xy=(20, 2.99), xytext=(23, 50), arrowprops={'facecolor': 'orange'})


# • y = 2**n and label it "O(2^n)"
y = [2**n for n in x]
plt.plot(x, y)
plt.annotate('$O(2^n)$', xy=(75, 37778931862957161709568), xytext=(70, 37778931862957161709568), arrowprops={'facecolor': 'purple'})


# • y = n! and label it "O(n!)"
y = [math.factorial(n) for n in x]
plt.plot(x, y)
plt.annotate('$O(n!)$', xy=(65, 8247650592082470666723170306785496252186258551345437492922123134388955774976000000000000000), xytext=(70, 8247650592082470666723170306785496252186258551345437492922123134388955774976000000000000000), arrowprops={'facecolor': 'magenta'})


# • y = n^n and label it "O(n^n)"
y = [n**n for n in x]
plt.plot(x,y)
plt.annotate('$O(n^n)$', xy=(80, 176684706477838432958329750074291851582748389687561895812160620129261977600000000000000000000000000000000000000000000000000000000000000000000000000000000), xytext=(70, 176684706477838432958329750074291851582748389687561895812160620129261977600000000000000000000000000000000000000000000000000000000000000000000000000000000), arrowprops={'facecolor': 'black'})


# title and x & y label code can come before or after plot

# #plt.plot(x, y, label = '$\mathcal[o](2^[x])$')

# 6. Bonus Write the code necessary to write your name on a chart. Use box letters.

# 7. Bonus: use curves for letters in your name that have curves in them.


# In[2]:


x = list(range(20, 81, 5))
print(x)


# In[ ]:





# In[3]:


σ

