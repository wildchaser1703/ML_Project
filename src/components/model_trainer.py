import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    GradientBoostingRegressor,
    AdaBoostRegressor,
    RandomForestRegressor
)

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
        trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
        def __init__(self):
                self.model_trainer_config = ModelTrainerConfig()
        def initiate_model_trainer(self, train_array, test_array):
                try:
                    logging.info("Split data into train and test data")
                    X_train, y_train, X_test ,y_test = (
                           train_array[:, :-1], 
                           train_array[:, -1],
                           test_array[:, :-1],
                           test_array[:, -1]
                    )
                    
                    models = {
                           "Linear Regression": LinearRegression(),
                           "KNeighbors Regressor": KNeighborsRegressor(),
                           "Decision Tree Regressor": DecisionTreeRegressor(),
                           "Random Forest Regressor": RandomForestRegressor(),
                           "XGBoost Regressor": XGBRegressor(),
                           "CatBoost Regressor": CatBoostRegressor(verbose = False),
                           "Gradient Boosting Regressor": GradientBoostingRegressor(),
                           "AdaBoost Regressor": AdaBoostRegressor(),
                    }

                    model_report: dict = evaluate_models(X_train = X_train, y_train = y_train, X_test = X_test,
                                                        y_test = y_test, models = models)
                    
                    #To get best model score from dict
                    best_model_score = max(sorted(model_report.values()))

                    #To get best model name from dict
                    best_model_name = list(model_report.keys())[
                        list(model_report.values()).index(best_model_score)]
                    best_model = models[best_model_name]

                    if best_model_score < 0.6:
                        raise CustomException("Best model score is less than 0.6")

                    logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")

                    save_object(
                        file_path = self.model_trainer_config.trained_model_file_path,
                        obj = best_model
                    )
                    logging.info("Model training completed successfully")

                    predicted = best_model.predict(X_test)
                    r2_square = r2_score(y_test, predicted)
                    logging.info(f"R2 score of the best model: {r2_square}")
                    return r2_square

                except Exception as e:
                    raise CustomException(e, sys)
                        
                