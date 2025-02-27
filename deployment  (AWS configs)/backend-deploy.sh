#!/bin/bash

# Package FastAPI for AWS Lambda
pip install -r backend/requirements.txt -t backend/

# Zip files for deployment
cd backend && zip -r function.zip . && cd ..

# Deploy Lambda function
aws lambda create-function \
    --function-name childcare-api \
    --runtime python3.9 \
    --role YOUR_AWS_LAMBDA_ROLE \
    --handler main.handler \
    --zip-file fileb://backend/function.zip