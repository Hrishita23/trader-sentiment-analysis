# Project Summary

## Methodology

This project analyzes trader behavior and market sentiment to identify behavioral patterns and estimate next-day profit and loss (PnL) volatility.

The trader behavior dataset and market sentiment dataset were first cleaned and merged into a unified dataset containing key trading metrics such as trade size (Size USD), risk level, trade direction (Side), and closed PnL. Missing values were handled and relevant features were engineered to summarize trader behavior.

To identify behavioral archetypes, traders were grouped using K-Means clustering. Before clustering, the features were standardized using StandardScaler so that variables with different scales contributed equally to the analysis. Traders were grouped into three clusters representing distinct trading styles.

Additionally, next-day PnL volatility was estimated to understand potential variability in trading outcomes. Visualizations and a lightweight dashboard built with Streamlit were used to explore and present the results.

---

## Key Insights

The clustering results indicate that traders naturally fall into distinct behavioral groups. One group tends to execute smaller trades with relatively stable returns, representing conservative trading behavior. Another group engages in larger trades and exhibits higher PnL volatility, indicating a more aggressive approach. A third group shows moderate trade sizes and mixed performance, suggesting opportunistic trading patterns.

The analysis also highlights that higher risk levels and larger trade sizes are often associated with greater PnL variability, reflecting increased exposure to market fluctuations.

---

## Strategy Recommendations

Based on the analysis, several recommendations can be made. Monitoring trader clusters can help identify high-risk trading behavior and enable better risk management controls. Limiting position sizes during periods of high volatility may reduce potential losses.

In addition, incorporating market sentiment indicators alongside trader behavior analysis could improve trading decisions. Finally, clustering-based monitoring systems can help detect shifts in trader behavior and allow platforms to adapt risk management strategies accordingly.
