import streamlit as st
import pandas as pd
import requests
import pickle
import json

with open ('preprocessing.pkl', 'rb') as f:
    preprocessing = pickle.load(f)

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io/',
        'Report a bug': "https://github.com/streamlit/streamlit/issues/new/choose",
        'About': ""
    }
)

st.title("Churn Prediction")
SeniorCitizen = st.selectbox('Senior Citizen', [1, 0])
Partner = st.selectbox('Partner', ['No', 'Yes'])
Dependents = st.selectbox('Dependents', ['No', 'Yes'])
PhoneService = st.selectbox('Phone Service', ['No', 'Yes'])
InternetService = st.selectbox('Internet Service', ['No', 'DSL', 'Fiber optic'])
OnlineSecurity = st.selectbox('Online Security', ['No', 'Yes', 'No internet service'])
OnlineBackup = st.selectbox('Online Backup', ['No', 'Yes', 'No internet service'])
DeviceProtection = st.selectbox('Device Protection', ['No', 'Yes', 'No internet service'])
TechSupport = st.selectbox('Tech Support', ['No', 'Yes', 'No internet service'])
StreamingTV = st.selectbox('Streaming TV', ['No', 'Yes', 'No internet service'])
StreamingMovies = st.selectbox('Streaming Movies', ['No', 'Yes', 'No internet service'])
MonthlyCharges = st.number_input('Monthly Charges', min_value=18.25, max_value=118.75)
Contract = st.radio('Contract', ['Month-to-month', 'One year', 'Two year'])
tenure = st.slider('Tenure', 0, 72)
st.write(tenure, 'Months')


# Inference
data = {'SeniorCitizen':SeniorCitizen,
        'Partner':Partner,
        'Dependents':Dependents,
        'tenure':tenure,
        'PhoneService':PhoneService,
        'InternetService':InternetService,
        'OnlineSecurity':OnlineSecurity,
        'OnlineBackup':OnlineBackup,
        'DeviceProtection':DeviceProtection,
        'TechSupport':TechSupport,
        'StreamingTV':StreamingTV,
        'StreamingMovies':StreamingMovies,
        'Contract':Contract,
        'MonthlyCharges':MonthlyCharges}

columns = ['SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'InternetService', 'OnlineSecurity',
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'MonthlyCharges']

data_inf = pd.DataFrame([data], columns=columns)
data_inf_final = preprocessing.transform(data_inf)
data_inf_final_list = data_inf_final.tolist()


input_data_json = json.dumps({
    'signature_name':'serving_default',
    'instances':data_inf_final_list
})

URL = 'https://malvin-subahri-p2m1-b.herokuapp.com/v1/models/model_func:predict' # URL heroku

if st.button('Predict'):
    r = requests.post(URL, data=input_data_json)
    result = r.json()
    if result['predictions'][0][0] > 0.5:
        st.markdown(
            '<h2 style="text-align: center"> Churn </h2>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<h2 style="text-align: center"> Not Churn </h2>',
            unsafe_allow_html=True,
        )