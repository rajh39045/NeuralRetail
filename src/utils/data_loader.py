import pandas as pd

def load_clean_data():
    return pd.read_csv(
        "../data/processed/cleaned_data.csv"
    )

def load_customer_segments():
    return pd.read_csv(
        "../data/features/customer_segments.csv"
    )

def load_forecast():
    return pd.read_csv(
        "../reports/forecasting/forecast_results.csv"
    )