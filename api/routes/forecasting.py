from fastapi import APIRouter
import pandas as pd

router = APIRouter(
    tags=["Demand Forecasting"]
)

@router.get("/forecast")
def get_forecast():

    forecast = pd.read_csv(
        "reports/forecasting/forecast_results.csv"
    )

    result = forecast[
        ["ds", "yhat"]
    ].tail(30)

    return result.to_dict(
        orient="records"
    )