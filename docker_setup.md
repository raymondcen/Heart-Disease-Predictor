## 1. Build Docker image
## 2. Setup GitHub Workflow from Github Actions
## 3. IAM user in AWS
## 4. Docker Setup in EC2
    - optional
        sudo apt-get update -y
        sudo apt-get upgrade
    - required
        curl -fsSl https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        newgrp docker
## 5. Setup runners in GitHub
## 6. Setup secret keys/variables in GitHub
    - 