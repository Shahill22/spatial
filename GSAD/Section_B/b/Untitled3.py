#!/usr/bin/env python
# coding: utf-8

# In[31]:


import geopandas as gpd


# In[32]:


data1 = gpd.read_file("D:\M.Sc.Computer Science GA\data\B\LABEXAM_SECTION_B\Data_02\Population_Kerala.csv")


# In[33]:


data2 = gpd.read_file("D:\M.Sc.Computer Science GA\data\B\LABEXAM_SECTION_B\Data_02\Kerala.shp")


# In[34]:


data2.crs


# In[35]:


data2_reproj = data2.to_crs("EPSG:32643")


# In[36]:


data2_reproj.crs


# In[37]:


data2_reproj


# In[38]:


data2_reproj['area'] = data2_reproj.area


# In[39]:


data2_reproj


# In[40]:


max_area = data2_reproj['area'].max


# In[41]:


max_area


# In[42]:


data2_reproj['pop_den']=data2_reproj['DistrictID'].astype(float)/data2_reproj['area'] 


# In[43]:


data2_reproj['pop_den']


# In[44]:


data2_reproj


# In[45]:


merge =  data2_reproj.merge(data1, on='District')

