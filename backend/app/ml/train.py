import pandas as pd
import pickle
from fbprophet import Prophet
import xgboost as xgb
import boto3
import os

def train_and_save_model():
    df = pd.read_csv("../../data/sample_sales_data.csv")
    df['ds'] = pd.to_datetime(df['date'])
    df['y'] = df['sales']

    # Prophet for trend
    m = Prophet(yearly_seasonality=True, weekly_seasonality=True)
    m.add_country_holidays(country_name='US')
    m.fit(df)

    # XGBoost for residuals
    df['residual'] = df['y'] - m.predict(df)['yhat']
    X = df[['temp', 'fuel_price', 'cpi', 'unemployment']]
    y = df['residual']
    xgb_model = xgb.XGBRegressor().fit(X, y)

    # Save locally
    m.save('prophet_model.pkl')
    with open('xgb_model.pkl', 'wb') as f:
        pickle.dump(xgb_model, f)

    # Upload to S3
    s3 = boto3.client('s3')
    bucket = "ai-erp-models-bucket"
    s3.upload_file('prophet_model.pkl', bucket, 'models/prophet.pkl')
    s3.upload_file('xgb_model.pkl', bucket, 'models/xgb.pkl')

    print("Model trained and uploaded to S3")

if __name__ == "__main__":
    train_and_save_model()
