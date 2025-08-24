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
            CovidPos: str
    ):
        pass