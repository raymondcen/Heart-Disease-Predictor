# Deploying with Azure Web App
## 1. Setup container registry
## 2. Docker setup in local and push to container registry
- Run in ternminal:
    - docker build -t loginservername.azurecr.io/resourcegroup:latest
    - docker login loginservername.azurecr.io
    - docker push loginservername.azurecr.io/resourcegroup:latest