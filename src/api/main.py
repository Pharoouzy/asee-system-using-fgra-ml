from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from .routes import estimate
from .routes import main
from .routes import healthcheck

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    default_message = 'An error occurred.'
    return JSONResponse(
        status_code=exc.status_code,
        content={'message': exc.detail if exc.detail else default_message, 'type': 'Error', 'path': str(request.url)},
    )

app.include_router(estimate.router, prefix='/api')
app.include_router(main.router)
app.include_router(healthcheck.router, prefix='/api')
