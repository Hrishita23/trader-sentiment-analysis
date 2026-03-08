import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Trader Behavior Dashboard")

data = pd.read_csv("trader_features.csv")

st.subheader("Dataset Preview")
st.dataframe(data.head())

st.subheader("Cluster Distribution")
st.bar_chart(data['cluster'].value_counts())

st.subheader("Trader Clusters")

fig, ax = plt.subplots()

ax.scatter(
    data['Size USD'],
    data['Closed PnL'],
    c=data['cluster']
)

ax.set_xlabel("Average Trade Size (USD)")
ax.set_ylabel("Average Closed PnL")

st.pyplot(fig)
