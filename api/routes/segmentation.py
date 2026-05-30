from fastapi import APIRouter
from api.schemas import SegmentRequest

import pandas as pd
import joblib

router = APIRouter(
    tags=["Customer Segmentation"]
)

pipeline = joblib.load(
    "models/segmentation_pipeline.pkl"
)

segment_map = {
    0: "New Customers",
    1: "VIP Customers",
    2: "Lost Customers",
    3: "Regular Customers"
}

@router.post("/predict-segment")
def predict_segment(data: SegmentRequest):

    sample = pd.DataFrame({
        "Recency": [data.recency],
        "Frequency": [data.frequency],
        "Monetary": [data.monetary]
    })

    cluster = int(
        pipeline.predict(sample)[0]
    )

    return {
        "cluster": cluster,
        "segment": segment_map.get(
            cluster,
            "Unknown"
        )
    }