from fastapi import FastAPI
from .routes import estimate
from .routes import main
from .routes import healthcheck

app = FastAPI()

app.include_router(estimate.router)
app.include_router(main.router)
app.include_router(healthcheck.router)