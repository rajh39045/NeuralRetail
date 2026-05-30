from fastapi import APIRouter
from api.schemas import ChurnRequest

import pandas as pd
import joblib

router = APIRouter(
    tags=["Churn Prediction"]
)

model = joblib.load(
    "models/churn_pipeline.pkl"
)

@router.post("/predict-churn")
def predict_churn(data: ChurnRequest):

    sample = pd.DataFrame({
        "Recency": [data.recency],
        "Frequency": [data.frequency],
        "Monetary": [data.monetary],
        "Cluster": [data.cluster]
    })

    prediction = model.predict(sample)[0]

    return {
        "churn_prediction": int(prediction)
    }