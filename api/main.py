from fastapi import FastAPI

from api.routes.churn import router as churn_router
from api.routes.segmentation import router as segmentation_router
from api.routes.forecasting import router as forecasting_router

app = FastAPI(
    title="NeuralRetail API",
    version="1.0.0",
    description="Retail Analytics API"
)

@app.get("/")
def home():
    return {
        "message": "NeuralRetail API Running"
    }

app.include_router(churn_router)
app.include_router(segmentation_router)
app.include_router(forecasting_router)