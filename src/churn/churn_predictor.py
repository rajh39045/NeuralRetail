import joblib
import pandas as pd

model = joblib.load(
    "../models/churn_pipeline.pkl"
)

def predict_churn(
    recency,
    frequency,
    monetary,
    cluster
):

    sample = pd.DataFrame({
        "Recency":[recency],
        "Frequency":[frequency],
        "Monetary":[monetary],
        "Cluster":[cluster]
    })

    return model.predict(sample)[0]