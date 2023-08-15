from fastapi import FastAPI, HTTPException
from .routes import estimate
from .routes import main
from .routes import healthcheck

app = FastAPI()

app.include_router(estimate.router, prefix='/api')
app.include_router(main.router)
app.include_router(healthcheck.router, prefix='/api')

@app.exception_handler(HTTPException)
def handle_exception(request, exc):
    return {
        'status_code': exc.status_code,
        'message': exc.detail
    }