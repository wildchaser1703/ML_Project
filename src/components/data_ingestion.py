import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.utils import save_object, evaluate_models
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts","train.csv")
    test_data_path : str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as a pandas dataframe")
            if not os.path.exists("notebook/data/stud.csv"):
                logging.error("File not found: notebook/data/stud.csv")
            cat_cols = df.select_dtypes(include=["object"]).columns
            for col in cat_cols:
                df[col] = (
                    df[col]
                    .replace({None: "None"})  # Replace Python None
                    .fillna("None")           # Replace NaN
                    .astype("category")       # Convert to categorical dtype
                )
            logging.info(f"Handled missing values and typecasting for columns: {list(cat_cols)}")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            df.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            logging.info("Ingestion of the data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data= obj.initiate_data_ingestion() 
    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data) 
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))