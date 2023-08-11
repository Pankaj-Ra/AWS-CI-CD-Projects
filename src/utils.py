import os
import sys

import numpy as np
import pandas as pd
import pickle
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.logger import logging
from src.exception import CustomException

"""After transformation Saved preprocessed data in pickle file
"""


def save_object(file_path, obj):
    try:
        dir_name = os.path.dirname(file_path)

        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, X_test, Y_train, Y_test, models, params):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]

            # model.fit(X_train, Y_train) #Train model

            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, Y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, Y_train)

            y_train_predict = model.predict(X_train)
            y_test_predict = model.predict(X_test)

            train_model_score = r2_score(Y_train, y_train_predict)
            test_model_score = r2_score(Y_test, y_test_predict)

            report[list(models.keys())[i]] = test_model_score

            return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as f_obj:
            return pickle.load(f_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
