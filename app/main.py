"""
Simple FastAPI application used to demonstrate a DevOps CI/CD pipeline.

This service provides a basic health endpoint that can be used
to verify deployments and container health.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevOps CI/CD pipeline is working!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}