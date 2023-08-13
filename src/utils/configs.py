import os
import yaml

PROJECT_ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
def load_yaml_file(filepath):
    with open(os.path.join(PROJECT_ROOT_DIR, filepath), 'r') as file:
        config = yaml.safe_load(file)
    return config

def general_configs():
    return load_yaml_file('configs/general_config.yaml')

def model_config():
    return load_yaml_file('configs/model_config.yaml')