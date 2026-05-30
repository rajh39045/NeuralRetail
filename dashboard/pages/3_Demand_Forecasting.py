import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Demand Forecasting")

forecast = pd.read_csv("reports/forecasting/forecast_results.csv")

metrics =pd.read_csv("reports/forecasting/forecast_metrics.csv")

col1,col2,col3 = st.columns(3)

col1.metric(
    "MAE",
    round(metrics["MAE"][0],2)
)

col2.metric(
    "RMSE",
    round(metrics["RMSE"][0],2)
)

col3.metric(
    "MAPE %",
    round(metrics["MAPE"][0],2)
)

fig = px.line(
    forecast,
    x="ds",
    y="yhat",
    title="Revenue Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)