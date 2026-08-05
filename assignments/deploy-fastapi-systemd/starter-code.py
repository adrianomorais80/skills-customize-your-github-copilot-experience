"""Starter code: Deploying FastAPI with systemd.

Run locally:
  pip install fastapi uvicorn
  uvicorn starter-code:app --host 0.0.0.0 --port 8000 --reload
"""

import os
from fastapi import FastAPI

app = FastAPI(title="Deployment Practice API")


@app.get("/")
def read_root():
    return {
        "message": "API online. Ready for deployment practice."
    }


@app.get("/health")
def health_check():
    # TODO: confirm in class that APP_ENV is set before production-like run
    app_env = os.getenv("APP_ENV", "development")
    return {
        "status": "ok",
        "environment": app_env
    }
