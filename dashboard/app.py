import streamlit as st
import pandas as pd
import plotly.express as px

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="NeuralRetail Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ================= LOAD DATA =================

rfm = pd.read_csv("data/features/customer_segments.csv")
cleaned = pd.read_csv("data/processed/cleaned_data.csv")

# ================= SIDEBAR =================

st.sidebar.title("🛒 NeuralRetail")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    AI-Powered Retail Analytics Platform

    Modules:
    • Customer Segmentation
    • Churn Prediction
    • Demand Forecasting
    """
)

# ================= HEADER =================

st.title("🛒 NeuralRetail Analytics Dashboard")

st.markdown(
    "Customer Segmentation • Churn Prediction • Demand Forecasting"
)

st.markdown("---")

# ================= KPI SECTION =================

total_customers = rfm["CustomerID"].nunique()

total_revenue = round(
    rfm["Monetary"].sum(),
    2
)

vip_customers = (
    rfm["Segment"] == "VIP Customers"
).sum()

lost_customers = (
    rfm["Segment"] == "Lost Customers"
).sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Revenue",
    f"₹ {total_revenue:,.0f}"
)

col3.metric(
    "VIP Customers",
    vip_customers
)

col4.metric(
    "Lost Customers",
    lost_customers
)

st.markdown("---")

# ================= CUSTOMER SEGMENTS =================

left, right = st.columns(2)

segment_count = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)

segment_count.columns = [
    "Segment",
    "Count"
]

fig1 = px.pie(
    segment_count,
    names="Segment",
    values="Count",
    hole=0.4,
    title="Customer Segment Distribution"
)

left.plotly_chart(
    fig1,
    use_container_width=True
)

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

right.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# ================= CHURN SECTION =================

st.subheader("📉 Customer Churn Overview")

rfm["Churn"] = (
    rfm["Recency"] > 90
).astype(int)

active_customers = (
    rfm["Churn"] == 0
).sum()

churned_customers = (
    rfm["Churn"] == 1
).sum()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Active Customers",
    active_customers
)

col2.metric(
    "Churned Customers",
    churned_customers
)

col3.metric(
    "Churn Rate %",
    round(
        churned_customers / len(rfm) * 100,
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

churn_df["Status"] = churn_df["Status"].map({
    0: "Active",
    1: "Churned"
})

fig3 = px.pie(
    churn_df,
    names="Status",
    values="Count",
    title="Active vs Churned Customers"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# ================= DATA PREVIEW =================

st.subheader("Customer Data Preview")

st.dataframe(
    rfm.head(20),
    use_container_width=True
)

# ================= FOOTER =================

st.markdown("---")

st.caption(
    "NeuralRetail Analytics Platform"
)