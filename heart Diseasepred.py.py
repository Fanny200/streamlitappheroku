# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 15:28:45 2023

@author: DELL
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models


loaded_model = pickle.load(open('C:/Users/DELL/Desktop/heart disease/saved model/heart_disease_model.sav','rb'))


input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          [
                           'Heart Disease Prediction',
                           ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
                         
                      
    
    
# Heart Prediction Page
