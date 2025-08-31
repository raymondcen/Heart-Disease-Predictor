# Deployment using CI/CD pipelines and GitHub Actions using AWS ECR2 and EC2 instance.    
## 1. Setup Dockerfile image
## 2. Setup GitHub Workflow (.github/workflow/main.yaml) from Github Actions
## 3. Setup IAM user in AWS and get access and secret access key
## 4. Setup ECR in AWS
## 4. Docker Setup in EC2 (ubuntu, t3.medium, setup/create key pair, allow all traffic)
    - optional
        sudo apt-get update -y
        sudo apt-get upgrade
    - required
        curl -fsSl https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        newgrp docker
## 5. Setup/create runner in GitHub. Execute code provided into EC2 instance
## 6. Setup secret keys/variables in GitHub
    - AWS access and secret key
    - AWS region
    - ECR URI and repo name
## 7. Test 