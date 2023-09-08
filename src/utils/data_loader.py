import os
from src.utils import configs

def load_raw_data() -> str:
    return get_file_path('raw')
def load_processed_data() -> str:
    return get_file_path('processed')
def load_interim_data() -> str:
    return get_file_path('interim')

def get_file_path(file_type: str):
    PROJECT_ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
    return os.path.join(PROJECT_ROOT_DIR, configs.general_configs()['data_paths'][file_type])