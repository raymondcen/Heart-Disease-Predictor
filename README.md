# Heart Disease Classification Project

## Overview
This project applies machine learning to predict the likelihood of heart disease using tabular patient data. It demonstrates the complete lifecycle of a data science project, starting from exploratory data analysis (EDA), to model training and tuning, to deployment in different environments. The goal was to practice not only building predictive models but also implementing them in production-ready pipelines and deploying them using modern cloud platforms.  

The project highlights:
- Use of structured healthcare-related data to classify heart disease risk.  
- Data preprocessing, feature analysis, and statistical exploration through EDA.  
- Model development using scikit-learn and tuning with multiple hyperparameter search methods.  
- A reusable prediction pipeline that handles preprocessing and model inference consistently.  
- Multiple cloud deployment strategies showing flexibility across AWS and Azure services.  

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
- Evaluated with metrics such as accuracy, precision, recall, and F1-score  

### 3. Hyperparameter Tuning
- RandomizedSearchCV for initial parameter sweeps  
- GridSearchCV for fine-tuning  
- Half Grid Search to balance performance and compute cost  

### 4. Prediction Pipeline
- Implemented an end-to-end pipeline for consistent preprocessing and prediction  
- Accepts raw input and outputs prediction (heart disease risk classification)  


## Deployment

### AWS (CodePipeline + Elastic Beanstalk + EC2 + GitHub)
- Automated CI/CD pipeline with AWS CodePipeline  
- Deployed to Elastic Beanstalk with an EC2 backend  
- Integrated with GitHub for continuous updates  
- [Deployment isntructions](https://github.com/raymondcen/Heart-Disease-Predictor/blob/aws-docker/deployment_setup.md)
### AWS (Docker + ECR)
- Containerized the application with Docker  
- Stored images in Elastic Container Registry (ECR)  
- Deployed to AWS infrastructure using Docker containers
- [Deployment instructions](google.com)

### Azure (Docker + Web App)
- Built Docker image for deployment  
- Pushed image to Azure Web App for Containers  
- Served predictions through the hosted web application
- [Deployment instructions](https://github.com/raymondcen/Heart-Disease-Predictor/blob/azure-docker/azure_docker_deployment.md)

Built with additional instructions from [Krish Naik YouTube](https://www.youtube.com/playlist?list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG)

