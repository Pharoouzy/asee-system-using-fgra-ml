import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from src.api.routes import healthcheck
    app.register_blueprint(healthcheck.bp)

    return app