import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_str


class PredictPipeline:
    def __init__(self):
        pass


class CustomData: #for mapping frontend inputs to backend
    def __init__(
            self,
            State: str,
            Sex: str,
            GeneralHealth: str,
            PhysicalHealthDays: float,
            MentalHealthDays: float,
            LastCheckupTime: str,
            PhysicalActivities: str,
            SleepHours: float,
            RemovedTeeth: str,
            HadHeartAttack: str,
            HadAngina: str,
            HadStroke: str,
            HadAsthma: str,
            HadSkinCancer: str,
            HadCOPD: str,
            HadDepressiveDisorder: str,
            HadKidneyDisease: str,
            HadArthritis: str,
            HadDiabetes: str,
            DeafOrHardOfHearing: str,
            BlindOrVisionDifficulty: str,
            DifficultyConcentrating: str,
            DifficultyWalking: str,
            DifficultyDressingBathing: str,
            DifficultyErrands: str,
            SmokerStatus: str,
            ECigaretteUsage: str,
            ChestScan: str,
            RaceEthnicityCategory: str,
            AgeCategory: str,
            HeightInMeters: float,
            WeightInKilograms: float,
            BMI: float,
            AlcoholDrinkers: str,
            HIVTesting: str,
            FluVaxLast12: str,
            PneumoVaxEver: str,
            TetanusLast10Tdap: str,
            HighRiskLastYear: str,
            CovidPos: str):
        
        self.State = State
        self.Sex = Sex
        self.GeneralHealth = GeneralHealth
        self.PhysicalHealthDays = PhysicalHealthDays
        self.MentalHealthDays = MentalHealthDays
        self.LastCheckupTime = LastCheckupTime
        self.PhysicalActivities = PhysicalActivities
        self.SleepHours = SleepHours
        self.RemovedTeeth = RemovedTeeth
        self.HadHeartAttack = HadHeartAttack
        self.HadAngina = HadAngina
        self.HadStroke = HadStroke
        self.HadAsthma = HadAsthma
        self.HadSkinCancer = HadSkinCancer
        self.HadCOPD = HadCOPD
        self.HadDepressiveDisorder = HadDepressiveDisorder
        self.HadKidneyDisease = HadKidneyDisease
        self.HadArthritis = HadArthritis
        self.HadDiabetes = HadDiabetes
        self.DeafOrHardOfHearing = DeafOrHardOfHearing
        self.BlindOrVisionDifficulty = BlindOrVisionDifficulty
        self.DifficultyConcentrating = DifficultyConcentrating
        self.DifficultyWalking = DifficultyWalking
        self.DifficultyDressingBathing = DifficultyDressingBathing
        self.DifficultyErrands = DifficultyErrands
        self.SmokerStatus = SmokerStatus
        self.ECigaretteUsage = ECigaretteUsage
        self.ChestScan = ChestScan
        self.RaceEthnicityCategory = RaceEthnicityCategory
        self.AgeCategory = AgeCategory
        self.HeightInMeters = HeightInMeters
        self.WeightInKilograms = WeightInKilograms
        self.BMI = BMI
        self.AlcoholDrinkers = AlcoholDrinkers
        self.HIVTesting = HIVTesting
        self.FluVaxLast12 = FluVaxLast12
        self.PneumoVaxEver = PneumoVaxEver
        self.TetanusLast10Tdap = TetanusLast10Tdap
        self.HighRiskLastYear = HighRiskLastYear
        self.CovidPos = CovidPos
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "State": [self.State],
                "Sex": [self.Sex],
                "GeneralHealth": [self.GeneralHealth],
                "PhysicalHealthDays": [self.PhysicalHealthDays],
                "MentalHealthDays": [self.MentalHealthDays],
                "LastCheckupTime": [self.LastCheckupTime],
                "PhysicalActivities": [self.PhysicalActivities],
                "SleepHours": [self.SleepHours],
                "RemovedTeeth": [self.RemovedTeeth],
                "HadHeartAttack": [self.HadHeartAttack],
                "HadAngina": [self.HadAngina],
                "HadStroke": [self.HadStroke],
                "HadAsthma": [self.HadAsthma],
                "HadSkinCancer": [self.HadSkinCancer],
                "HadCOPD": [self.HadCOPD],
                "HadDepressiveDisorder": [self.HadDepressiveDisorder],
                "HadKidneyDisease": [self.HadKidneyDisease],
                "HadArthritis": [self.HadArthritis],
                "HadDiabetes": [self.HadDiabetes],
                "DeafOrHardOfHearing": [self.DeafOrHardOfHearing],
                "BlindOrVisionDifficulty": [self.BlindOrVisionDifficulty],
                "DifficultyConcentrating": [self.DifficultyConcentrating],
                "DifficultyWalking": [self.DifficultyWalking],
                "DifficultyDressingBathing": [self.DifficultyDressingBathing],
                "DifficultyErrands": [self.DifficultyErrands],
                "SmokerStatus": [self.SmokerStatus],
                "ECigaretteUsage": [self.ECigaretteUsage],
                "ChestScan": [self.ChestScan],
                "RaceEthnicityCategory": [self.RaceEthnicityCategory],
                "AgeCategory": [self.AgeCategory],
                "HeightInMeters": [self.HeightInMeters],
                "WeightInKilograms": [self.WeightInKilograms],
                "BMI": [self.BMI],
                "AlcoholDrinkers": [self.AlcoholDrinkers],
                "HIVTesting": [self.HIVTesting],
                "FluVaxLast12": [self.FluVaxLast12],
                "PneumoVaxEver": [self.PneumoVaxEver],
                "TetanusLast10Tdap": [self.TetanusLast10Tdap],
                "HighRiskLastYear": [self.HighRiskLastYear],
                "CovidPos": [self.CovidPos],
            }
        
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
