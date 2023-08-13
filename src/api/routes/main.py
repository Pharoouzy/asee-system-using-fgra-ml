from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def estimate():
    return { 'status': 'success', 'message': 'Welcome to Software Effort Estimation API' }