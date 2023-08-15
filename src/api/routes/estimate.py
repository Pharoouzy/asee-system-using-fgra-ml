import os
import joblib
from fastapi import APIRouter, HTTPException
from src.api.models.story_model import StoryModel
from datetime import datetime
from src.utils import configs

# model = load_trained_model()

router = APIRouter()

@router.post('/estimate')
async def estimate(data: StoryModel):
    try:
        # TODO: Add the feature names to estimate from the model
        # features = [data.feature_name1, data.feature_name2, ...]  # Add all the feature names
        # prediction = model.predict([features])
        # return {'status': 'success', 'data': prediction[0] }
        current_timestamp = datetime.now().isoformat()
        return {
            'status': 'success',
            'message': 'Effort estimation successful',
            'timestamp': current_timestamp,
            'model_version': '1.0.0',
            'data': { 'estimated_effort': 12.5 },
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def load_trained_model() -> object:
    try:
        project_root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
        model_path: str = os.path.join(project_root_dir, configs.general_configs()['artifact_paths']['model'])
        # Load the trained model
        return joblib.load(model_path)
    except Exception as e:
        raise e