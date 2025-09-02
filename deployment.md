# Deployment with AWS Elastic Beanstalk
## 1. Setup .ebextensions/python.config
## 2. Create AWS Elastic Beanstalk web app
 - Add AWSElasticbeanstalkService to permission policies in roles
 - Add a .ebignore to specify files and directories that should be excluded from the source bundle created for deployment to Elastic Beanstalk environments.
## 3. Create AWS Codepipeline and deploy
- Integrate with GitHub