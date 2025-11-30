import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str= os.path.join('artifacts', 'test.csv')
    raw_data_path: str= os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # sub oject creation
        # three paths are created in artifacts folder when above line is executed
    def initiate_data_ingestion(self):
        # if data stored in some database or cloud storage, code to fetch data will be written here
        logging.info("Entered the data ingestion method or component")
        try:
            # this dataset is just for example, you can replace it with your own dataset
            # it can be read from database or cloud storage also or api
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')
            
            # since aritfacts folder may not be present, we create it
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # saving raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            # train test split
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            # saving train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            # returning the file paths
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
           raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
