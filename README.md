# CSE291_AWS_Analysis

## GreenGrader

- `./greengrader/task_execution_scripts`: contains the scripts used for trigger tasks/container on AWS ECS.
  - Usage -
    - cd in to `./greengrader/task_execution_scripts` and run `./trigger_tasks.sh <number_of_tasks>`
    - The URLs for Fargate and EC2 are different, one should be commented.
- `./greengrader/graph_scripts`: contains the scripts used for generating graphs.
- `./source_code`: contains source code for GreenGrader application.

## Image Object Detection

### Relevant Files

- `./image_object_detection/code/inderence.py`: main inference script.

  - Model_fn - load the model
  - Input_fn - take input and process it for the model
  - Predict_fn - pass processed inputs through model to get prediction
  - Output_fn - process the predictions and return the results

- `./image_object_detection/code/requirements.txt`: all dependencies needed for the project

### Provisioned

- `./image_object_detection/provisioned/1_Deployment_*.ipynb`: download YOLOv8 model, zip inference code and model to S3, create SageMaker provisioned (standard or compute optimized) endpoint and deploy it
- `./image_object_detection/provisioned/2_TestEndpoint_*.ipynb`: Test the deployed endpoint by running an image and plotting output; Cleanup the endpoint and hosted model

### Serverless

- `./image_object_detection/serverless/1_Deployment_serverless.ipynb`: download YOLOv8 model, zip inference code and model to S3, create SageMaker serveless endpoint and deploy it
- `./image_object_detection/serverless/2_TestEndpoint_serverless.ipynb`: Test the deployed endpoint by running an image and plotting output; Cleanup the endpoint and hosted model
