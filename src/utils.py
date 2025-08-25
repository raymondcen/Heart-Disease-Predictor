import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, HalvingGridSearchCV

from src.exception import CustomException
from src.logger import logging

import json


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models,params):
    try:
        report = {}

        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]

            params_model=params.get(model_name, {})

            logging.info(f"Begin tuning and training for {model_name}")
            #fine tune, find best hyperparamters
            # gs = RandomizedSearchCV(
            #         model, 
            #         params_model, 
            #         n_iter = 25,
            #         cv=3, 
            #         n_jobs=4, 
            #         scoring="f1",
            #         random_state=42,
            # )
            # gs = HalvingGridSearchCV(
            #             estimator=model,
            #             param_grid=params_model,
            #             factor=3,                    # Keep top 1/3 at each iteration
            #             min_resources=1000,          #Start with 1k samples
            #             max_resources=len(X_train),  #Use all data for final candidates
            #             cv=5,                        
            #             scoring="f1",
            #             n_jobs=4,                   
            #             random_state=42,
            # )
            # gs = GridSearchCV(
            #         model, 
            #         params_model, 
            #         cv=5, 
            #         n_jobs=5, 
            #         scoring="f1",
            # )

            # gs.fit(X_train, y_train)
            # model.set_params(**gs.best_params_)

            #train
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            logging.info(f"Finished tuning and training for {model_name}")

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
                # "best_params": gs.best_params_,
                "train": train_metrics,
                "test": test_metrics
            }

        return report

    except Exception as e:
        raise CustomException(e, sys)
    

def save_model_report_json(model_report: dict, base_path: str):
    """
    Saves model report as JSON with a sequential filename.
    
    base_path: e.g., 'notebook/data/model_trainer_results.json'
    """
    os.makedirs(os.path.dirname(base_path), exist_ok=True)

    # Find next available sequential filename
    dir_name = os.path.dirname(base_path)
    base_name = os.path.splitext(os.path.basename(base_path))[0]
    ext = ".json"
    
    existing_files = [f for f in os.listdir(dir_name) if f.startswith(base_name) and f.endswith(ext)]
    existing_indices = []
    for f in existing_files:
        parts = f.replace(ext, "").split("_")
        if parts[-1].isdigit():
            existing_indices.append(int(parts[-1]))
    next_index = max(existing_indices, default=0) + 1

    new_file_name = f"{base_name}_{next_index}{ext}"
    full_path = os.path.join(dir_name, new_file_name)

    # Prepare JSON
    json_report = {}
    for model_name, scores in model_report.items():
        json_report[model_name] = {
            "best_params": scores.get("best_params", {}),
            "train_metrics": {k: round(v, 4) for k, v in scores["train"].items()},
            "test_metrics": {k: round(v, 4) for k, v in scores["test"].items()}
        }

    with open(full_path, "w") as f:
        json.dump(json_report, f, indent=4)

    logging.info(f"Model evaluation results saved to {full_path}")
    return full_path
