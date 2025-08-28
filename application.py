from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app=application

# Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    # print("Form data received:")
    # for key, value in request.form.items():
    #     print(f"{key}: '{value}'")
    if request.method=='GET':
        return render_template('fields.html')
    else:
        data=CustomData(
            Sex = request.form.get('Sex'),
            GeneralHealth = request.form.get('GeneralHealth'),
            PhysicalHealthDays = float(request.form.get('PhysicalHealthDays')),
            MentalHealthDays = float(request.form.get('MentalHealthDays')),
            LastCheckupTime = request.form.get('LastCheckupTime'),
            PhysicalActivities = request.form.get('PhysicalActivities'),
            SleepHours = float(request.form.get('SleepHours')),
            RemovedTeeth = request.form.get('RemovedTeeth'),
            HadHeartAttack = request.form.get('HadHeartAttack'),
            HadAngina = request.form.get('HadAngina'),
            HadStroke = request.form.get('HadStroke'),
            HadAsthma = request.form.get('HadAsthma'),
            HadSkinCancer = request.form.get('HadSkinCancer'),
            HadCOPD = request.form.get('HadCOPD'),
            HadDepressiveDisorder = request.form.get('HadDepressiveDisorder'),
            HadKidneyDisease = request.form.get('HadKidneyDisease'),
            HadArthritis = request.form.get('HadArthritis'),
            HadDiabetes = request.form.get('HadDiabetes'),
            DeafOrHardOfHearing = request.form.get('DeafOrHardOfHearing'),
            BlindOrVisionDifficulty = request.form.get('BlindOrVisionDifficulty'),
            DifficultyConcentrating = request.form.get('DifficultyConcentrating'),
            DifficultyWalking = request.form.get('DifficultyWalking'),
            DifficultyDressingBathing = request.form.get('DifficultyDressingBathing'),
            DifficultyErrands = request.form.get('DifficultyErrands'),
            SmokerStatus = request.form.get('SmokerStatus'),
            ECigaretteUsage = request.form.get('ECigaretteUsage'),
            ChestScan = request.form.get('ChestScan'),
            RaceEthnicityCategory = request.form.get('RaceEthnicityCategory'),
            AgeCategory = request.form.get('AgeCategory'),
            HeightInMeters = float(request.form.get('HeightInMeters')),
            WeightInKilograms = float(request.form.get('WeightInKilograms')),
            BMI = float(request.form.get('BMI')),
            AlcoholDrinkers = request.form.get('AlcoholDrinkers'),
            HIVTesting = request.form.get('HIVTesting'),
            FluVaxLast12 = request.form.get('FluVaxLast12'),
            PneumoVaxEver = request.form.get('PneumoVaxEver'),
            TetanusLast10Tdap = request.form.get('TetanusLast10Tdap'),
            HighRiskLastYear = request.form.get('HighRiskLastYear'),
            CovidPos = request.form.get('CovidPos')

        )

        predictions_df=data.get_data_as_dataframe()
        print(predictions_df)

        predict_pipeline=PredictPipeline()
        results = predict_pipeline.predict(predictions_df)
        if results[0] == 0:
            msg = "you DO NOT have heart disease."
        else:
            msg = "you DO have heart disease."
        return render_template('fields.html', results=msg)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=8080)