from aws_cdk import aws_sagemaker as sagemaker

class SageMakerStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        model = sagemaker.CfnModel(
            self, "SalesForecastModel",
            execution_role_arn="arn:aws:iam::123:role/SageMakerRole",
            primary_container=sagemaker.CfnModel.ContainerDefinitionProperty(
                image="763104351884.dkr.ecr.us-east-1.amazonaws.com/xgboost:latest",
                model_data_url="s3://ai-erp-models-bucket/models/"
            )
        )
