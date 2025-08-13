import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path= os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info('Splitting training and test input data')
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1],
            )

            models = {
                "Logistic Regression": LogisticRegression(n_jobs=-1),
                "Random Forest": RandomForestClassifier(n_jobs=-1),
                "Decision Tree": DecisionTreeClassifier(),  # single-thread only
                "XGBoost": XGBClassifier(n_jobs=-1, tree_method="hist"),  # hist = faster
                "CatBoost": CatBoostClassifier(verbose=False, thread_count=-1),
                "AdaBoost": AdaBoostClassifier(),  # single-thread only
                "GradientBoosting": GradientBoostingClassifier(),  # single-thread only
                "K-Nearest Neighbors": KNeighborsClassifier(n_jobs=-1),
            }
            
            model_report:dict=evaluate_models(
                X_train=X_train, y_train=y_train, 
                X_test = X_test, y_test = y_test, 
                models=models
            )

            ## best model name and f1 score
            best_model_name = max(model_report, key=lambda m: model_report[m]["test"]["f1"])
            best_model_score = model_report[best_model_name]["test"]["f1"]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info("Best model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

            predicted = best_model.predict(X_test)
            f1 = f1_score(y_test, predicted, zero_division=0)

            return f1

        except Exception as e:
            raise CustomException(e,sys)
