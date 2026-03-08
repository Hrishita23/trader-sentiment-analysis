# Trader Behavior & Market Sentiment Analysis

## Project Overview

This project analyzes trader behavior and market sentiment to identify behavioral patterns, cluster traders into archetypes, and estimate next-day profit and loss (PnL) volatility.

Using historical trading activity and sentiment data, we explore how trader actions relate to market conditions and identify strategies that could improve trading performance.

---

## Objectives

The main goals of this project are:

* Analyze trading activity and behavioral metrics of traders
* Identify trader archetypes using clustering techniques
* Examine the relationship between market sentiment and trader performance
* Estimate next-day PnL volatility
* Provide strategy insights based on the analysis
* Build a lightweight dashboard to explore the results

---


### Download Dataset

Download the dataset from the link below:

Dataset Link:
1) Bitcoin Market Sentiment (Fear/Greed)
Columns: Date, Classification (Fear / Greed)
Link: https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing

2) Historical Trader Data (Hyperliquid)
Includes fields like: account, symbol, execution price, size, side, time, start position, event, closedPnL, leverage, etc.
Link: https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing

After downloading, place the dataset files in the project directory.
---
Explanation:

analysis.ipynb → main analysis notebook
app.py → Streamlit dashboard
outputs/ → generated charts and visualizations
summary.md → one-page methodology and insights

---

## Methodology

The project follows these main steps:

1. **Data Preprocessing**

   * Clean and merge trader behavior and sentiment datasets
   * Handle missing values
   * Encode categorical variables

2. **Feature Engineering**
   Key features used:

   * Average trade size
   * Risk level
   * Trade direction (buy/sell)
   * Closed PnL

3. **Trader Clustering**
   Traders are grouped into behavioral archetypes using
   K-Means clustering.

4. **Volatility Estimation**
   PnL volatility is calculated to estimate next-day variability in trader profit and loss.

5. **Visualization**
   Charts are created to explore clusters and trader patterns.

6. **Interactive Dashboard**
   A lightweight Streamlit dashboard allows exploration of the results.

---

## Installation

Install required Python libraries:

```
pip install pandas numpy scikit-learn matplotlib streamlit
```

---

## Running the Analysis

Open the notebook and run all cells:

Trader_Sentiment_Analysis.ipynb

This notebook performs:

* Data preprocessing
* Feature engineering
* Trader clustering
* Volatility estimation
* Visualization generation

---

## Running the Streamlit Dashboard (Google Colab)

Since the dashboard is executed inside Google Colab, a public URL is required to access the Streamlit interface. This is done using **ngrok**.

### Step 1: Create an ngrok Account

1. Go to https://ngrok.com
2. Create a free account
3. Copy your **ngrok authentication token**

### Step 2: Install Required Packages

Run the following in Google Colab:

pip install streamlit pyngrok

### Step 3: Add Your ngrok Token

In your notebook, run:

from pyngrok import ngrok
ngrok.set_auth_token("YOUR_NGROK_TOKEN")

Note: Replace `"YOUR_NGROK_TOKEN"` with your personal token.

### Step 4: Run the Dashboard

streamlit run app.py

After running the command, ngrok will generate a **public URL** where the Streamlit dashboard can be accessed.

Example:

https://random-id.ngrok-free.app

Open this link in your browser to interact with the dashboard.
---

## Key Visualization

Example cluster visualization:

(cluster_plot1.png)

This plot shows traders grouped into behavioral clusters based on trade size and profitability.

---

## Insights

Key findings from the analysis include:

* Traders can be grouped into distinct behavioral archetypes.
* Aggressive traders tend to have larger trade sizes and higher PnL volatility.
* Conservative traders show more stable but smaller returns.
* Market sentiment appears to influence trading direction and risk levels.

---

## Technologies Used

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Streamlit

---

## Author

Project completed as part of a data analysis and machine learning assignment.
