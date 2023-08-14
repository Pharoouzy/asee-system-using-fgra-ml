import sys
from src.utils.exception import CustomException
from src.utils.logger import logger
import os
from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from src.utils import configs

load_dotenv()

USERNAME = os.environ.get('MYSQL_USERNAME')
PASSWORD = os.environ.get('MYSQL_PASSWORD')
HOST = os.environ.get('MYSQL_HOST')
DATABASE = os.environ.get('MYSQL_DATABASE')

DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

query = '''
SELECT 
    i.*,
    r.Name Repository_Name,
    p.Name Poject_Name
FROM Issue i
JOIN Project p 
ON i.Project_ID = p.ID
JOIN Repository r 
ON p.Repository_ID = r.ID;
'''

class DataIngestion:
    PROJECT_ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
    def __init__(self):
        self.raw_data_path: str = os.path.join(DataIngestion.PROJECT_ROOT_DIR, configs.general_configs()['data_paths']['raw'])

    def ingest(self, reload: bool = False) -> str:
        logger.info("Started data ingestion process...")
        try:
            if Path(self.raw_data_path).exists() and not reload:
                logger.info(f"Data already ingested to CSV: {self.raw_data_path}")
                return self.raw_data_path

            with create_engine(DATABASE_URI).connect() as connection:
                chunk_size = 800000
                chunks = pd.read_sql(query, connection, chunksize=chunk_size)

                first_chunk = True
                for chunk in chunks:
                    if chunk.isnull().values.any():
                        logger.warning("Warning: Found missing data!")

                    if first_chunk:
                        chunk.to_csv(self.raw_data_path, index=False, mode='w', escapechar='\\')
                        first_chunk = False
                    else:
                        chunk.to_csv(self.raw_data_path, index=False, mode='a', escapechar='\\')
                logger.info(f"Data successfully ingested to CSV: {self.raw_data_path}")

            return self.raw_data_path
        except Exception as e:
            raise CustomException(e, sys)