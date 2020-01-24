#!/usr/bin/env python
# coding: utf-8

# In[73]:


import numpy as np
import matplotlib.pyplot as plt


# In[74]:


#implementacja metody Eulera dla podanego równania różniczkowego y'= f(x) = 2*x*(y – 1) przy założeniach, że
#y(x=0) = 2 i x<2, 3>. 


def eul(min_x,max_x,h):
    
    x=np.arange(min_x,max_x,h)
    x_1=len(x)
    
    y=np.zeros(x_1)
    y[0]=2
    
    for i in range(x_1-1):
        y[i+1]=y[i]+h*fun(x[i],y[i])
    
    
    
    print(x)
    print(y)
    
    plt.plot(x,y)
    plt.title("Metoda Eulera")    
    

def fun(x,y):
    
    dy=2*x*(y-1)
    
    return dy


# In[75]:


fun(2,3)

eul(2,3,0.1)


# In[76]:


# implementacja metody Rungego-Kutty (te same założenia)


def run(min_x,max_x,h):
    
    x=np.arange(min_x,max_x,h)
    x_2=len(x)
    
    y=np.zeros(x_2)
    y[0]=2
    
    for i in range(x_2-1):
        y[i+1]=y[i]+h*fun(x[i]+h/2,y[i]+h/2*fun(x[i],y[i]))
        
   
    print(x)
    print(y)
    
    plt.plot(x,y)
    plt.title("Metoda Rungego-Kutty") 
    


# In[77]:


fun(2,3)

run(2,3,0.1)


# In[ ]:




