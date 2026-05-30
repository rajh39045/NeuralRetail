import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Customer Segmentation")

rfm = pd.read_csv("data/features/customer_segments.csv")

segment_count = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)

segment_count.columns = [
    "Segment",
    "Customers"
]

fig = px.pie(
    segment_count,
    names="Segment",
    values="Customers",
    hole=0.4,
    title="Customer Segment Distribution"
)

st.plotly_chart(fig, use_container_width=True)

segment_revenue = (
    rfm.groupby("Segment")["Monetary"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    segment_revenue,
    x="Segment",
    y="Monetary",
    color="Segment",
    title="Revenue Contribution by Segment"
)

st.plotly_chart(fig2, use_container_width=True)

st.dataframe(rfm.head(20))