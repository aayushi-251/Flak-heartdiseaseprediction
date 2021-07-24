from flask_cors import cross_origin
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@cross_origin()
@app.route('/')
def index():
    return render_template('index1.html')


@cross_origin()
@app.route('/predict', methods=['POST'])
def predict():
    Male = float(request.form['Male'])
    Age = float(request.form['Age'])
    CurrentSmoker = float(request.form['CurrentSmoker'])
    CigsPerDay = float(request.form['CigsPerDay'])
    BPMeds = float(request.form['BPMeds'])
    PrevalentStroke = float(request.form['PrevalentStroke'])
    PrevalentHyp = float(request.form['PrevalentHyp'])
    Diabetes = float(request.form['Diabetes'])
    TotalChol = float(request.form['TotalChol'])
    sysBP = float(request.form['sysBP'])
    DiaBP = float(request.form['DiaBP'])
    BMI = float(request.form['BMI'])
    HeartRate = float(request.form['HeartRate'])
    GlucoseLevel = float(request.form['GlucoseLevel'])

    # loading the model file from the storage
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    # predictions using the loaded model file
    prediction = loaded_model.predict([[Male, Age, CurrentSmoker, CigsPerDay, BPMeds, PrevalentStroke, PrevalentHyp,
                                        Diabetes, TotalChol, sysBP, DiaBP, BMI, HeartRate, GlucoseLevel]])
    if prediction == [1]:
        prediction = "Risk of CoronaryHeartDisease"
    else:
        prediction = "Normal, no risk of CoronaryHeartDisease"
    return render_template('result.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
