# Deploying with Azure Web App
## 1. Setup Azure container registry
## 2. Docker setup in local and push to Azure container registry
- Run in ternminal:
    - docker build -t loginservername.azurecr.io/resourcegroup:latest
    - docker login loginservername.azurecr.io
    - docker push loginservername.azurecr.io/resourcegroup:latest
## 3.