import pandas as pd

def get_forecast():
    return pd.read_csv(
        "../reports/forecasting/forecast_results.csv"
    )