import streamlit as st
import requests

st.set_page_config(
    page_title="Going To College Prediction",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io/',
        'Report a bug': "https://github.com/streamlit/streamlit/issues/new/choose",
        'About': ""
    }
)

st.title("Going To College Prediction")
type_school = st.selectbox('School', ['Academic', 'Vocational'])
school_accreditation = st.selectbox('Accreditation', ['A', 'B'])
interest = st.selectbox('Interest', ['Not Interested', 'Less Interested', 'Uncertain', 'Interested', 'Very Interested'])
residence = st.selectbox('Residence', ['Urban', 'Rural'])
parent_salary = st.number_input('Parent Salary')
house_area = st.number_input('House Area')
average_grades = st.number_input('Average Grades')

# Inference
data = {'type_school':type_school,
        'school_accreditation':school_accreditation,
        'interest':interest,
        'residence':residence,
        'parent_salary':parent_salary,
        'house_area':house_area,
        'average_grades':average_grades}

# URL = "http://127.0.0.1:5000/college_prediction" # comment sebelum push backend
URL = "https://malvin-subahri-ftds-012-p1m2-b.herokuapp.com/college_prediction" # URL heroku


# Komunikasi
r = requests.post(URL, json=data)
res = r.json()
if st.button('Predict'):
    st.title(res['result']['label_name'])
else:
    st.title("")