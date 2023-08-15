from datetime import datetime
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def home():
    return {
        'status': 'success',
        'message': 'Welcome to Software Effort Estimation API',
        'timestamp': datetime.now().isoformat(),
        'model_version': '1.0.0',
    }