#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


import streamlit as st


# In[3]:


dataset='train.csv'
image='Classification.png'


# In[14]:


#@st.cache
def load_data(dataset):
    df = pd.read_csv(dataset)
    return df


# In[7]:


def load_description(df):
        # Preview of the dataset
        st.header("Data Preview")
        preview = st.radio("Choose Head/Tail?", ("Top", "Bottom"))
        if(preview == "Top"):
            st.write(df.head())
        if(preview == "Bottom"):
            st.write(df.tail())

        # display the whole dataset
        if(st.checkbox("Show complete Dataset")):
            st.write(df)

        # Show shape
        if(st.checkbox("Display the shape")):
            st.write(df.shape)
            dim = st.radio("Rows/Columns?", ("Rows", "Columns"))
            if(dim == "Rows"):
                st.write("Number of Rows", df.shape[0])
            if(dim == "Columns"):
                st.write("Number of Columns", df.shape[1])

        # show columns
        if(st.checkbox("Show the Columns")):
            st.write(df.columns)


# In[8]:


def load_viz(df):
        st.header("Data Visualisation")
        st.subheader("Seaborn - countplot")
        fig = plt.figure()
        sns.countplot(x='output', data=df)
        st.pyplot(fig)


# In[11]:


def main():

    # Title/ text
    st.title("Classification")
    st.image(image, use_column_width = True)

    # loading the data
    df = load_data(dataset)

    # display description
    load_description(df)

    #visualis
    load_viz(df)


# In[12]:


if(__name__ == '__main__'):
    main()


# In[ ]:





# In[ ]:




