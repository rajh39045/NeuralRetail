import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📉 Churn Analysis")

rfm = pd.read_csv("data/features/customer_segments.csv")

rfm["Churn"] = (
    rfm["Recency"] > 90
).astype(int)

active = (rfm["Churn"] == 0).sum()
churned = (rfm["Churn"] == 1).sum()

col1,col2,col3 = st.columns(3)

col1.metric(
    "Active Customers",
    active
)

col2.metric(
    "Churned Customers",
    churned
)

col3.metric(
    "Churn Rate %",
    round(
        churned / len(rfm) * 100,
        2
    )
)

churn_df = (
    rfm["Churn"]
    .value_counts()
    .reset_index()
)

churn_df.columns = [
    "Status",
    "Count"
]

churn_df["Status"] = (
    churn_df["Status"]
    .map({
        0:"Active",
        1:"Churned"
    })
)

fig = px.pie(
    churn_df,
    names="Status",
    values="Count",
    title="Churn Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)