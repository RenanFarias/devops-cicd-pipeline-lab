# DevOps CI/CD Pipeline Lab

This project demonstrates a basic DevOps CI/CD workflow using:

- Python FastAPI
- Docker
- GitHub Actions

The pipeline automatically:

- validates application code
- installs dependencies
- builds a Docker image

## Application Endpoints
GET /

Returns a welcome message.

GET /health

Returns the service health status.

## Container Image

The CI pipeline automatically builds and publishes a Docker image to GitHub Container Registry.

Image location:

ghcr.io/<username>/devops-cicd-pipeline-lab/devops-cicd-demo:latest