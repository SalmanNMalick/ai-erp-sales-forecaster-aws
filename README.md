# AI-Powered ERP System with Sales Forecasting & ROI Prediction on AWS

Fully serverless, scalable AI ERP with ML forecasting using **AWS SageMaker + Prophet + XGBoost**.

## Features
- Sales prediction per SKU (next 30/90 days)
- ROI forecasting per product/campaign
- Inventory optimization suggestions
- Real-time dashboard
- Secure JWT auth
- Deployed on AWS (API Gateway, Fargate, RDS, S3, SageMaker)

## Tech Stack
- Backend: **FastAPI** (Python)
- Database: **PostgreSQL on RDS**
- ML: **Prophet + XGBoost + SageMaker**
- Infra: **AWS CDK (Python)**
- CI/CD: **GitHub Actions**
- Storage: **S3**
- Hosting: **ECS Fargate + API Gateway**

## Quick Start

```bash
# Clone and deploy
git clone https://github.com/yourusername/ai-erp-sales-forecaster-aws.git
cd ai-erp-sales-forecaster-aws

# Install CDK
npm install -g aws-cdk
pip install -r infrastructure/requirements.txt

# Bootstrap CDK (once)
cdk bootstrap aws://ACCOUNT-ID/REGION

# Deploy everything
cd infrastructure/cdk
cdk deploy --all
