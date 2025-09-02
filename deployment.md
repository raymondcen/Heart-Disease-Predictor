# Deployment using CI/CD pipelines and GitHub Actions using AWS ECR2 and EC2 instance.    
## 1. Setup Dockerfile image
## 2. Setup GitHub Workflow 
- GitHub Actions has a template
- .github/workflow/main.yaml from Github Actions
## 3. Setup IAM user in AWS and get access and secret access key
- Add appropriate EC2 and EC2 permissions
## 4. Create and setup a new ECR in AWS
## 5. Create and setup a EC2 instance 
- ubuntu, t3.medium, setup/create key pair, allow all traffic etc.
### 5.1 Once setup, connect to the instance and run the following in the terminal
- Optional
```
    sudo apt-get update -y
    sudo apt-get upgrade
```
- Required
```
    curl -fsSl https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
```
## 6. Create and setu runner in GitHub. 
### 6.1 Execute code provided into EC2 instance terminal
## 6. Setup secret keys/variables in GitHub
  - AWS access and secret key from IAM user
  - AWS region
  - ECR URI and repo name
## 7. Test 