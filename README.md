# CSE291_AWS

## Image Object Detection

### Relevant Files

- ```./image_object_detection/code/inderence.py```: 
- ```./image_object_detection/code/requirements.txt```: all dependencies needed for the project

### Provisioned
- ```./image_object_detection/provisioned/1_Deployment_*.ipynb```: download YOLOv8 model, zip inference code and model to S3, create SageMaker provisioned (standard or compute optimized) endpoint and deploy it
- ```./image_object_detection/provisioned/2_TestEndpoint_*.ipynb```: Test the deployed endpoint by running an image and plotting output; Cleanup the endpoint and hosted model

### Serverless
- ```./image_object_detection/serverless/1_Deployment_serverless.ipynb```: download YOLOv8 model, zip inference code and model to S3, create SageMaker serveless endpoint and deploy it
- ```./image_object_detection/serverless/2_TestEndpoint_serverless.ipynb```: Test the deployed endpoint by running an image and plotting output; Cleanup the endpoint and hosted model
