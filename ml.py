#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
from sklearn.svm import SVC
from pickle import dump, load


# In[14]:


import streamlit as st


# In[8]:


from pickle import dump, load

def predict(arr):

    # Loading pretrained svm_rbf classifier from pickle file
    classifier = load(open('svmRBF_Model.pickle', 'rb'))

    # Prediction
    prediction = classifier.predict(arr)

    return prediction


# In[9]:


def main():
    Value_1=st.number_input('Enter Value_1 :')
    Value_2=st.number_input('Enter Value_2 :')
    arr = np.array([Value_1,Value_2]).reshape(1,-1)

    prediction = predict(arr)
    click = st.button("SUBMIT")

    if click:
        if(arr.any()):
            st.subheader("Prediction:")
        if(prediction == 0):
            st.write("Negative :cry:")
        else:
            st.write("Positive :sunglasses:")




# In[10]:


if(__name__ == '__main__'):
    main()

