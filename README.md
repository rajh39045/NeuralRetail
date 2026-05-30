# 🛒 NeuralRetail Analytics Platform

## Overview

NeuralRetail is an AI-powered retail analytics platform developed using the Online Retail II dataset.

The platform provides:

* Customer Segmentation using RFM Analysis and K-Means Clustering
* Customer Churn Prediction using XGBoost
* Demand Forecasting using Prophet
* Interactive Business Dashboard using Streamlit

The objective is to help retail businesses understand customer behavior, identify churn risks, and forecast future demand.

---

## Features

### Customer Segmentation

Customers are segmented into:

* VIP Customers
* Loyal Customers
* New Customers
* Lost Customers

Segmentation is performed using:

* Recency
* Frequency
* Monetary Value (RFM)

and K-Means clustering.

---

### Churn Prediction

A churn prediction model was developed using:

* Recency
* Frequency
* Monetary Value
* Cluster Information

Algorithm:

* XGBoost Classifier

Performance:

* Accuracy: 99.54%
* Precision: 99.65%
* Recall: 98.95%
* F1 Score: 99.30%

---

### Demand Forecasting

Future revenue demand is forecasted using:

* Prophet Time Series Forecasting

Evaluation Metrics:

* MAE: 23907.40
* RMSE: 27086.51
* MAPE: 66.16%

---

### Dashboard

Interactive Streamlit Dashboard includes:

* Executive KPI Overview
* Customer Segmentation Analysis
* Churn Analysis
* Demand Forecasting Insights

---

## Dataset

Dataset Used:

Online Retail II Dataset

Columns:

* Invoice
* StockCode
* Description
* Quantity
* InvoiceDate
* Price
* Customer ID
* Country

---

## Tech Stack

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-Learn
* XGBoost

### Forecasting

* Prophet

### Dashboard

* Streamlit

---

## Project Structure

NeuralRetail/

├── dashboard/

├── data/

│   ├── raw/

│   ├── processed/

│   └── features/

├── models/

│   ├── churn/

│   └── forecasting/

├── notebooks/

├── reports/

├── src/

└── README.md

---

## Future Improvements

* Real-Time Forecasting
* Inventory Optimization
* MLflow Experiment Tracking
* FastAPI Deployment
* Model Monitoring
* Drift Detection

---

## Author

Harsh Raj

Computer Science & Engineering
