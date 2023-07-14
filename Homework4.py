







#def is of list comp filetrs 3 and 4

# %%
def list_comp1(lst):
 
    comp_list=list(filter(lambda x:x%4==0 or x%3==0 ,lst)) 
    return [ele for ele in comp_list]
    raise NotImplementedError()



#this function above is list generator



# %%
def list_comp2(lst):
   
    comp_list=list(map(lambda x:x*3 if(x%2==0) else x*5,lst))
    return [ele for ele in comp_list]
    raise NotImplementedError()


# In[25]:




# In[26]:


assert list_comp2(range(200, 220)) == [600, 1005, 606, 1015, 612, 1025, 618,
                                       1035, 624, 1045, 630, 1055, 636, 1065, 642, 1075, 648, 1085, 654, 1095]


# In[3]:


