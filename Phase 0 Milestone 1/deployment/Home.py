import pandas as pd
import plotly.express as px
import streamlit as st
import datetime

def app ():
    st.title('Google Ads Campaign !!!')

    st.header('Type of Ads')
    selected_radio = st.radio('Select One', 
                            ['Text', 'Video', 'Image'])
    if selected_radio == 'Text':
        st.write('Our Most Favourite !')
    elif selected_radio == 'Video':
        st.write('Our Most Premium !')
    else:
        st.write('Our Most Economic !')  

    st.header('Region')
    st.multiselect('Choose Country Subdivision',
        ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Washington, D.C.', 'Delaware', 'Florida',
         'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts',
         'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska',
         'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
         'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia',
         'Wyoming'])

    st.header('Duration')
    slide = st.slider('Your Ads Will Last For', 0, 365)
    st.write(slide, 'Days')

    if st.button('Submit'):
        st.write('Your Data is Being Processed')
