import joblib
import pandas as pd

pipeline = joblib.load(
    "../models/segmentation_pipeline.pkl"
)

def predict_segment(
    recency,
    frequency,
    monetary
):
    sample = pd.DataFrame({
        "Recency":[recency],
        "Frequency":[frequency],
        "Monetary":[monetary]
    })

    return pipeline.predict(sample)[0]