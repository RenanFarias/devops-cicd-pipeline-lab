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