import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

import yaml
from collections import Counter

import numpy as np



from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models, save_model_report_json

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
            

            
            #xgboost imbalance
            from collections import Counter

            counter = Counter(y_train)
            n_negative = counter[0]
            n_positive = counter[1]

            scale_pos_weight = n_negative / n_positive

            models = {
                # "Logistic Regression": LogisticRegression(
                #     max_iter=2000,
                #     class_weight='balanced',
                #     random_state=42,
                #     C=0.2,
                #     penalty="l2",
                #     solver="saga"                    
                # ),
                # "Random Forest": RandomForestClassifier(
                #     class_weight='balanced',
                #     bootstrap=True,
                #     random_state=42,
                #     max_depth= 15,
                #     max_features= "sqrt",
                #     max_leaf_nodes= 150,
                #     min_samples_leaf= 6,
                #     min_samples_split= 5,
                #     n_estimators= 75,

                # ),
                "XGBoost": XGBClassifier(
                    scale_pos_weight=scale_pos_weight,
                    tree_method="hist", 
                    random_state=42,
                    eval_metric='logloss',
                    colsample_bytree = 0.7,
                    learning_rate= 0.05,
                    max_depth = 3,
                    n_estimators = 50,
                    subsample = 0.6,
                ), 
                # "CatBoost": CatBoostClassifier(
                #     verbose=False,
                #     auto_class_weights='Balanced',
                #     random_state=42,
                #     # iterations=1000,
                #     eval_metric='Logloss',
                #     depth =5,
                #     iterations = 300,
                #     l2_leaf_reg=15,
                #     learning_rate= 0.05,
                # ),
                # "GradientBoosting": GradientBoostingClassifier(

                # )
            }

    
            #get params
            with open("src/components/params.yaml", "r") as f:
                params=yaml.safe_load(f)


            logging.info('Evaluating models')
            model_report:dict=evaluate_models(
                X_train=X_train, y_train=y_train, 
                X_test = X_test, y_test = y_test, 
                models=models,
                params=params
            )
            logging.info('Done evaluating models')

            #save report
            report_file = os.path.join("src/components/model_tuned_results", "model_tuned_results.json")
            save_model_report_json(model_report, report_file)

            ## best model name and f1 score
            best_model_name = max(model_report, key=lambda m: model_report[m]["test"]["f1"])
            best_model_score = model_report[best_model_name]["test"]["f1"]

            best_model = models[best_model_name]

            # if best_model_score < 0.6:
            #     raise CustomException("No best model found")

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
