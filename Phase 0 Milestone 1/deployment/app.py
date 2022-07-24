import Home
import Visualisasi
import Statistical_Analysis
import streamlit as st

st.set_page_config(
    page_title="Google Ads Campaign",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io/',
        'Report a bug': "https://github.com/streamlit/streamlit/issues/new/choose",
        'About': ""
    }
)

PAGES = {'Home': Home,
         'Data Visualization': Visualisasi,
         'Statistical Analysis': Statistical_Analysis}

st.sidebar.title ('Menu')
selected = st.sidebar.selectbox ('Select Page: ', ['Home', 'Data Visualization', 'Statistical Analysis'])

page = PAGES [selected]

page.app ()
