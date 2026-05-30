# 🛒 NeuralRetail Analytics Platform

## 🚀 Overview

NeuralRetail Analytics Platform is an end-to-end AI-powered retail analytics solution developed using the Online Retail II dataset. The platform combines customer intelligence, machine learning, time-series forecasting, and interactive business analytics to help retail organizations make data-driven decisions.

The platform enables businesses to:

* Identify high-value customers
* Predict customer churn
* Forecast future sales and demand
* Visualize business insights through an interactive dashboard
* Access machine learning models through REST APIs

---

## 🌟 Key Features

### 👥 Customer Segmentation

Implemented RFM (Recency, Frequency, Monetary) Analysis and K-Means Clustering to classify customers into meaningful business segments:

* ⭐ VIP Customers
* 🤝 Loyal Customers
* 🆕 New Customers
* ⚠️ Lost Customers

**Business Value:**

* Personalized marketing campaigns
* Improved customer retention
* Revenue optimization

---

### 📉 Customer Churn Prediction

Built a machine learning model to identify customers likely to stop purchasing.

**Features Used**

* Recency
* Frequency
* Monetary Value
* Customer Cluster

**Algorithm**

* XGBoost Classifier

**Model Performance**

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 99.54% |
| Precision | 99.65% |
| Recall    | 98.95% |
| F1 Score  | 99.30% |

---

### 📈 Demand Forecasting

Implemented time-series forecasting using Prophet to predict future revenue trends.

**Algorithm**

* Prophet Forecasting Model

**Evaluation Metrics**

| Metric | Value     |
| ------ | --------- |
| MAE    | 23,907.40 |
| RMSE   | 27,086.51 |
| MAPE   | 66.16%    |

**Business Value**

* Inventory planning
* Revenue forecasting
* Demand estimation

---

### 📊 Interactive Analytics Dashboard

Developed a Streamlit dashboard for business users.

Dashboard Modules:

* Executive KPI Overview
* Customer Segmentation Analysis
* Churn Analysis
* Demand Forecasting Insights
* Revenue Analytics

---

## 🌐 Live Deployment

### Dashboard

https://neuralretail-analytics.streamlit.app/

### FastAPI Backend

https://neuralretail-api-f1g9.onrender.com

### API Documentation

https://neuralretail-api-f1g9.onrender.com/docs

### GitHub Repository

https://github.com/rajh39045/NeuralRetail

---

## 🗂 Dataset Information

**Dataset:** Online Retail II Dataset

**Total Records:** 500,000+ Transactions

### Features

| Column      |
| ----------- |
| Invoice     |
| StockCode   |
| Description |
| Quantity    |
| InvoiceDate |
| Price       |
| Customer ID |
| Country     |

---

## 🛠 Technology Stack

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-Learn
* XGBoost

### Time Series Forecasting

* Prophet

### Backend Development

* FastAPI
* Uvicorn

### Dashboard

* Streamlit

### Deployment

* Render
* Streamlit Community Cloud

---

## 🏗 Project Architecture

```text
Online Retail II Dataset
            │
            ▼
      Data Cleaning
            │
            ▼
     Feature Engineering
        (RFM Analysis)
            │
 ┌──────────┼──────────┐
 │          │          │
 ▼          ▼          ▼
Customer   Churn    Demand
Segment.  Prediction Forecasting
 │          │          │
 └──────────┼──────────┘
            ▼
         FastAPI
            ▼
      Streamlit Dashboard
            ▼
      Business Insights
```

---

## 📁 Project Structure

```text
NeuralRetail/
│
├── api/
├── dashboard/
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
│
├── docs/
├── models/
├── notebooks/
├── reports/
├── src/
│
├── requirements.txt
├── README.md
├── render.yaml
└── runtime.txt
```

---

## 🔮 Future Enhancements

* Real-Time Forecasting
* Inventory Optimization System
* MLflow Experiment Tracking
* Automated Model Retraining
* Drift Detection
* Recommendation Engine
* Docker Containerization
* CI/CD Integration

---

## 👨‍💻 Author

**Abhishek Kumar**

Computer Science & Engineering

### Connect

* GitHub: https://github.com/rajh39045

---

