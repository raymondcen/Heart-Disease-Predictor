# Heart Disease Classification Project

## Overview
This project focuses on building and deploying a **machine learning model** to classify the likelihood of heart disease from tabular patient data.  
The workflow includes **data exploration (EDA)**, **model training**, **hyperparameter tuning**, and **deployment** across multiple cloud environments.


## Tech Stack
- **Python**
- **Jupyter Notebooks**
- **scikit-learn**
- **NumPy**
- **pandas**
- **Docker**


## Project Workflow

### 1. Exploratory Data Analysis (EDA)
- Inspected dataset structure and distributions  
- Handled missing values and categorical features  
- Created visualizations to understand relationships between features and target  

### 2. Model Training
- Built classification models using scikit-learn  
- Evaluated with metrics such as **accuracy, precision, recall, and F1-score**  

### 3. Hyperparameter Tuning
- **RandomizedSearchCV** for initial parameter sweeps  
- **GridSearchCV** for fine-tuning  
- **Half Grid Search** to balance performance and compute cost  

### 4. Prediction Pipeline
- Implemented an end-to-end pipeline for consistent preprocessing and prediction  
- Accepts raw input and outputs prediction (heart disease risk classification)  


## Deployment

### AWS (CodePipeline + Elastic Beanstalk + EC2 + GitHub)
- Automated CI/CD pipeline with **AWS CodePipeline**  
- Deployed to **Elastic Beanstalk** with an **EC2** backend  
- Integrated with GitHub for continuous updates  
- [Deployment isntructions](https://github.com/raymondcen/Heart-Disease-Predictor/blob/aws-docker/deployment_setup.md)
### AWS (Docker + ECR)
- Containerized the application with **Docker**  
- Stored images in **Elastic Container Registry (ECR)**  
- Deployed to AWS infrastructure using Docker containers
- [Deployment instructions](google.com)

### Azure (Docker + Web App)
- Built Docker image for deployment  
- Pushed image to **Azure Web App for Containers**  
- Served predictions through the hosted web application
- [Deployment instructions](https://github.com/raymondcen/Heart-Disease-Predictor/blob/azure-docker/azure_docker_deployment.md)

Built with additional instructions from [https://www.youtube.com/playlist?list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG]

