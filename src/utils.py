import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

from src.exception import CustomException

import json

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models,params):
    try:
        report = {}

        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]

            params=params.get(model_name, {})

            #fine tune, find best hyperparamters
            gs = RandomizedSearchCV(
                    model, 
                    params, 
                    n_inter=50,
                    cv=3, 
                    n_jobs=-1, 
                    scoring="f1",
                    random_state=42,
                )
            gs.fit(X_train, y_train)

            #train
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Train metrics
            train_metrics = {
                "accuracy": accuracy_score(y_train, y_train_pred),
                "precision": precision_score(y_train, y_train_pred, zero_division=0),
                "recall": recall_score(y_train, y_train_pred, zero_division=0),
                "f1": f1_score(y_train, y_train_pred, zero_division=0)
            }

            # Test metrics
            test_metrics = {
                "accuracy": accuracy_score(y_test, y_test_pred),
                "precision": precision_score(y_test, y_test_pred, zero_division=0),
                "recall": recall_score(y_test, y_test_pred, zero_division=0),
                "f1": f1_score(y_test, y_test_pred, zero_division=0)
            }

            # Store both
            report[model_name] = {
                "best_params": gs.best_params_,
                "train": train_metrics,
                "test": test_metrics
            }

        return report

    except Exception as e:
        raise CustomException(e, sys)
    

def save_model_report_json(model_report: dict, file_path: str):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    json_report = {}
    for model_name, scores in model_report.items():
        json_report[model_name] = {
            "best_params": scores.get("best_params", {}),
            "train_metrics": {k: round(v, 4) for k, v in scores["train"].items()},
            "test_metrics": {k: round(v, 4) for k, v in scores["test"].items()}
        }

    with open(file_path, "w") as f:
        json.dump(json_report, f, indent=4)

    print(f"Model evaluation results saved to {file_path}")