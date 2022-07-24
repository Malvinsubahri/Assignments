from flask import Flask, request, jsonify
import pickle
import pandas as pd 

# Inisiasi
app = Flask (__name__)

# Open model
def open_model (model_path):
    """
    helper function for loading model
    """
    with open (model_path, 'rb') as f:
        model = pickle.load (f)
    return model

model_knn_gs = open_model ("model.pkl")

# Fungsi untuk inference
def inference_college (data, model):
    """
    input : pandas dataframe
    output : predicted class (True, False)
    """
    LABEL = ["False", "True"]
    columns = ['type_school', 'school_accreditation', 'interest', 'residence', 'parent_salary', 'house_area', 'average_grades']
    data = pd.DataFrame ([data], columns=columns)
    res = model.predict (data)
    return res [0], LABEL [res[0]]

# Halaman Home
@app.route ("/")
def homepage ():
    return "<h1> Backend Milestone 2 </h1>" 

# Halaman inference
@app.route('/college_prediction', methods = ['POST'])
def college_predict ():
    """
    content = 
    {
        'type_school' : Academic / Vocational,
        'school_accreditation' : A / B,
        'interest' : Not Interested / Less Interested / Uncertain / Interested / Very Interested,
        'residence' : Urban / Rural,
        'parent_salary' : xx,
        'house_area' : xx,
        'average_grades' : xx
    }
    """
    content = request.json
    newdata = [
        content['type_school'],
        content['school_accreditation'],
        content['interest'],
        content['residence'],
        content['parent_salary'],
        content['house_area'],
        content['average_grades']
               ]
    res_idx, res_label = inference_college(newdata, model_knn_gs)
    result = {
        'label_idx' : str(res_idx),
        'label_name' : res_label
    }
    response = jsonify(success=True,
                       result=result)
    return response, 200

# Run app di local
# Jika deploy di heroku, comment baris di bawah ini 
# app.run (debug=True)