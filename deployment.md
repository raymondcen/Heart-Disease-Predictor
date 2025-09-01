Web application
    - column names dont need to match preprocessor.pkl but would be more helpful when matching
    - all values (value="") present in fields HTML form needs to match whats in preprocessor.pkl
Deployment
    - /.ebextensions/python.config
    - using AWS Elastic Beanstalk
        - instanced server/cloud enviorment
        - might need to create roles if just starting out
    - create a code pipeline (CodePipeline) between GitHub repository and Elastic Beanstalk
        - continuous delivery pipeline
    - CodePipeline
        - Build custom pipeline option
        - source provider: 
    - EB enviorment
        - need to allow more permissions
            - add AWSElasticbeanstalkService to permission policies in roles
