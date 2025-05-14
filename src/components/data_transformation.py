import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    def __init__(self):
        pass

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):

        '''
        This function is responsible for the following steps of data transformation:
        1. Handling missing values
        2. Standard scaling of numerical columns
        3. One hot encoding of categorical columns
        4. Creating a preprocessor object using ColumnTransformer
        5. Saving the preprocessor object to a file
        6. Returning the preprocessor object
        7. Logging the information about the columns and the preprocessor object
        8. Handling exceptions
        9. Returning the preprocessor object
        10. Logging the information about the columns and the preprocessor object
        '''

        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = ["gender", 
                                   "race_ethnicity", 
                                   "parental_level_of_education", 
                                   "lunch", 
                                   "test_preparation_course"]
            
            num_pipeline = Pipeline(steps = [
                ("imputer", SimpleImputer(strategy = "median")),
                ("scaler", StandardScaler())
            ])

            logging.info("Numerical columns standard scaling completed")
            logging.info(f"Numerical Columns are : {numerical_columns}")

            cat_pipeline = Pipeline(steps = [
                ("imputer", SimpleImputer(strategy = "most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
                ])
        
            logging.info("Categorical columns standard scaling completed")
            logging.info(f"Categorical Columns are : {categorical_columns}")

            preprocessor = ColumnTransformer(
                transformers = [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            logging.info("Preprocessor object created")

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    # start data transormation on datasets
    def initiate_data_transformation(self, train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Train and test dataframes read successfully")
            logging.info("Obtaining preprocessor object")
            preprocessor_obj = self.get_data_transformer_object()
            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_features_train_df = train_df.drop(columns = [target_column_name], axis = 1)
            target_feature_train_df = train_df[target_column_name]
            input_features_test_df = test_df.drop(columns = [target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Train and test dataframes split into input and target features")

            # Transforming the input features
            input_features_train_arr = preprocessor_obj.fit_transform(input_features_train_df)
            input_features_test_arr = preprocessor_obj.transform(input_features_test_df)
            logging.info("Input features transformed successfully")

            # Converting the target features into numpy arrays
            train_arr = np.c_[input_features_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_features_test_arr, np.array(target_feature_test_df)]     

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path = self.data_transformation_config.preprocessor_ob_file_path,
                obj = preprocessor_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)


        