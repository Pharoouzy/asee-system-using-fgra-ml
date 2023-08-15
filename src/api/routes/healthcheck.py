from datetime import datetime
from fastapi import APIRouter

router = APIRouter()

@router.get('/healthcheck')
async def healthcheck():
    return {
        'status': 'OK',
        'message': 'Software Effort Estimation API is working!',
        'timestamp': datetime.now().isoformat(),
        'model_version': '1.0.0',
    }