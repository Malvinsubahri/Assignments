import streamlit as st
import requests
from PIL import Image
import json
import numpy as np
import tensorflow as tf
from io import BytesIO


st.set_page_config(
    page_title="Fresh Meat Prediction",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io/',
        'Report a bug': "https://github.com/streamlit/streamlit/issues/new/choose",
        'About': ""
    }
)

st.title("Fresh Meat Prediction")

def img_predict(img):
    pred = np.array(img)[:, :, :3]
    pred = tf.image.resize(pred, size=(200, 200))
    pred = pred / 255.0

    image_tensor = tf.expand_dims(pred, 0)
    image_tensor = image_tensor.numpy().tolist()
    

    input_data_json = json.dumps({
    'signature_name':'serving_default',
    'instances':image_tensor
                                })
    URL = "https://backendp2m2.herokuapp.com/v1/models/model_ft:predict"
    r=requests.post(URL,data= input_data_json)
    res=r.json()

    list = ['Fresh', 'Half', 'Spoiled']
    prediction = list[(np.array(res['predictions'][0]).argmax())]
    st.header (prediction)

# Image Upload Option
 
file = st.file_uploader("Upload an image...", type=["jpg", "png", 'Tiff'])
if file is not None:
    img = Image.open(file)

col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    submitted = st.button('Predict')

    
if submitted:
    img_predict(img)