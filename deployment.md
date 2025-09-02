# Deploying with Azure Web App and Docker
## 1. Create and setup Dockerfile
## 2. Create and setup a Azure Container registry
- You will also need to create a resource group if you do not already have one
- Enable 'Admin user' in Access Keys tab
## 3. Docker setup in local and push to Azure container registry
- Run in ternminal:
```
    docker build -t containerregistryname.azurecr.io/resourcegroup:latest
    docker login containerregistryname.azurecr.io
    docker push containerregistryname.azurecr.io/resourcegroup:latest
```
## 4. Create and setup Azure Web App in App Services
- Publish from Container
- Connect it to correct container registry
- Once setup go into Deployment Center and enable 'Continuous deployment'
## 5. Setup workflow in GitHub Actions
- GitHub Actions will provide a template for GHCR instead of ACR.
- Follow the instructions but you will need to change anything associated to GHCR URLs/hooks to ACR URL/hooks

