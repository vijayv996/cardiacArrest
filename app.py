from flask import Flask, request, render_template
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('cardiac_arrest_prediction_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = float(request.form['age'])
        gender = int(request.form['gender'])
        smoking = int(request.form['smoking'])
        hypertension = int(request.form['hypertension'])
        stroke = int(request.form['stroke'])
        ap_hi = float(request.form['ap_hi'])
        ap_lo = float(request.form['ap_lo'])
        bmi = float(request.form['bmi'])
        hr = float(request.form['hr'])
        glucose = float(request.form['glucose'])
        metabolicSyndrome = float(request.form['metabolicSyndrome'])
        exerciseAngina = float(request.form['exerciseAngina'])
        fastingBloodSugar = float(request.form['fastingBloodSugar'])
        usesStimulantDrugs = float(request.form['usesStimulantDrugs'])
        input_data = [[gender,age,smoking,stroke,hypertension,ap_hi,ap_lo,bmi,hr,glucose,exerciseAngina,fastingBloodSugar,usesStimulantDrugs,metabolicSyndrome]]
        prediction = model.predict(input_data)
        statement = ''
        if prediction==1:
            statement = "Cardiac arrest may occur."
            color = "red"
        elif prediction==0:
            statement = "Cardiac arrest may not occur."
            color = "green"
        # statement+=str(prediction)
        return render_template('prediction.html', prediction=statement, colour = color)
    else:
        return render_template('form.html')
