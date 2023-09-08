import joblib
import os
from src.utils.logger import logger
def save_model(model):
    PROJECT_ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
    model_path = os.path.join(PROJECT_ROOT_DIR, 'artifacts/models/effort_estimation_model.joblib')
    joblib.dump(model, model_path)
    logger.info(f"Model successfully saved to: {model_path}")