import sys
from src.utils.exception import CustomException
from src.utils.logger import logger
import os
import csv
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

PROJECT_ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')

def ingest_raw_data(reload: bool = False) -> str:
    query: str = 'SELECT * FROM Issue;'
    raw_data_path: str = os.path.join(PROJECT_ROOT_DIR, configs.general_configs()['data_paths']['raw'])
    logger.info('Started data ingestion process...')
    try:
        if Path(raw_data_path).exists() and not reload:
            logger.info(f'Data already ingested to CSV: {raw_data_path}')
            return raw_data_path

        with create_engine(DATABASE_URI).connect() as connection:
            chunk_size = 800000
            chunks = pd.read_sql(query, connection, chunksize=chunk_size)

            first_chunk = True
            for chunk in chunks:
                if chunk.isnull().values.any():
                    logger.warning("Warning: Found missing data!")

                if first_chunk:
                    chuck_to_csv(path=raw_data_path, chunk=chunk, mode='w')
                    first_chunk = False
                else:
                    chuck_to_csv(path=raw_data_path, chunk=chunk)

            logger.info(f"Data successfully ingested to CSV: {raw_data_path}")

        return raw_data_path
    except Exception as e:
        raise CustomException(e, sys)

def chuck_to_csv(path: str, chunk: pd.DataFrame, mode: str = 'a') -> None:
    chunk.to_csv(path, mode=mode, index=False, header=mode == 'w', quoting=csv.QUOTE_MINIMAL, escapechar='\\')