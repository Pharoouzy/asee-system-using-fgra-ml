import os
import joblib
from fastapi import APIRouter, HTTPException
from src.api.models.story_model import StoryModel
from datetime import datetime
from src.utils import configs
from joblib import load

model = load(configs.general_configs()['artifact_paths']['model'])

router = APIRouter()

@router.post('/estimate')
async def estimate(data: StoryModel):
    try:
        current_timestamp = datetime.now().isoformat()
        if model:
            features = [
                data.Description,
                data.Title,
                data.Sprint_ID,
                data.Status,
            ]
            prediction = model.predict([features])
            if not prediction:
                raise HTTPException(status_code=400, detail='Could not estimate story point.')

            response = {
                'status': 'success',
                'message': 'Effort estimation successful',
                'timestamp': current_timestamp,
                'model_version': '1.0.0',
                'data': (prediction[0])
            }
        else:
            response =  {
                'status': 'success',
                'message': 'Effort estimation successful [test]',
                'timestamp': current_timestamp,
                'model_version': '1.0.0',
                'data': { 'estimated_effort': 12.5 },
            }

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def load_trained_model() -> object:
    try:
        project_root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
        model_path: str = os.path.join(project_root_dir, configs.general_configs()['artifact_paths']['model'])
        # Load the trained model
        return joblib.load(model_path)
    except Exception as e:
        raise e