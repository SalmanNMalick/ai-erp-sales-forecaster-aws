#!/bin/bash
python backend/app/ml/train.py

aws sagemaker create-model \
    --model-name sales-forecast-v2 \
    --primary-container Image=763104351884.dkr.ecr.us-east-1.amazonaws.com/xgboost:latest,ModelDataUrl=s3://ai-erp-models-bucket/models/ \
    --execution-role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/SageMakerRole
