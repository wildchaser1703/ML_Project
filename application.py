from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from logging import FileHandler, WARNING
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__, template_folder="templates")
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
application.logger.addHandler(file_handler)  

app = application

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score') or 0),
            writing_score=float(request.form.get('writing_score') or 0)
        )
        pred_df = data.get_data_as_data_frame()
        app.logger.info("DataFrame ready for prediction")
        
        predict_pipeline = PredictPipeline()
        app.logger.info("PredictPipeline initialized")
        
        results = predict_pipeline.predict(pred_df)
        app.logger.info("Prediction complete")
        
        return render_template('home.html', results=results[0])
