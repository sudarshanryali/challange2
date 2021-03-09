#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import data as da
import ml as ma


# In[5]:


def main():
    # EDA
    da.main()

    st.header("SVM_RBF Predictor")

    # Predictor
    ma.main()


# In[6]:


if(__name__ == '__main__'):
    main()


# In[ ]:




