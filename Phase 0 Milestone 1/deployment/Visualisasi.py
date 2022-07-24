import streamlit as st
import numpy as np
import pandas as pd

def app ():
    st.title ('Data Visualization')
    st.write ('This is Page For Data Visualization Dashboard')

    data = pd.read_csv('h8dsft_Milestone1_Malvin_Subahri.csv')
    if st.checkbox('Show RAW Data'):
        st.subheader('RAW Data')
        st.write (data)

    st.header ('Most Popular Type of Ads')
    st.image ('ad_type.png')

    st.header ('Average Duration of Ads in A Day')
    st.image ('num_of_days.png')

    st.header ('Ads Distributions and Impressions')
    st.image ('dist_imp.png')

    st.header ('Average Ads Costs')
    st.image ('ratarata.png')
    
    st.header ('Ads Estimation Costs For Campaign')
    st.write ('Option 1: Image & Text - 7 Days - 51 Regions')
    st.write ('Option 2: Image & Video - 7 Days - 51 Regions')
    st.write ('Option 3: Image - 7 Days - 51 Regions')
    st.image ('biaya.png')

    st.header ('Rate This Page')
    st.select_slider('Anwer', ['Awesome', 'Outstanding', 'Magnificent'])

    if st.button('Submit'):
        st.write('Thanks For Rating')
    
