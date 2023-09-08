import os
from fastapi import APIRouter, HTTPException
from src.api.models.story_model import StoryModel
from datetime import datetime
from src.utils import configs
from joblib import load
from src.api.utils.transformers import transform_request_data
import numpy as np

def load_model() -> object:
    try:
        project_root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..')
        model_path: str = os.path.join(project_root_dir, configs.general_configs()['artifact_paths']['model'])
        # Load the trained model
        return load(model_path)
    except Exception as e:
        raise e

model = load_model()

router = APIRouter()

@router.post('/estimate')
async def estimate(data: StoryModel):
    try:
        current_timestamp = datetime.now().isoformat()
        if model:
            # Transform request data
            transformed_data = transform_request_data(data)
            X = [list(transformed_data.values())]
            prediction = model.predict(X)

            if not prediction:
                raise HTTPException(status_code=400, detail='Could not estimate story point.')

            return {
                'status': 'success',
                'message': 'Effort estimation successful',
                'timestamp': current_timestamp,
                'model_version': '1.0.0',
                'estimation': np.round(prediction[0], 3)
            }
        else:
            raise HTTPException(status_code=500, detail='Unable to estimate story point at this time, please try again later.')

    except Exception as e:
        raise HTTPException(status_code=500, detail=e.detail)
