# E-Commerce Funnel Drop-Off Analysis

## Project Overview

This project examines user behavior on an e-commerce platform using the RetailRocket events dataset, with the goal of identifying where in the purchase funnel users drop off and uncovering the root causes behind low conversion rates.

The workflow combines:
- **Python** (Jupyter) for KPI computation, exploratory analysis, and root cause diagnostics.
- **Tableau** for building an interactive dashboard that communicates insights clearly to stakeholders.

The findings translate into data-driven, actionable recommendations aimed at improving conversion rates and reducing funnel leakage.

[View Interactive Dashboard](https://public.tableau.com/views/E-CommerceFunnelInsightsDashboard/E-CommerceFunnelInsightsConversionDrop-OffDiagnostics?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

![Dashboard screenshot](./reports/E-Commerce%20Funnel%20Insights%20Conversion%20Drop-Off%20Diagnostics.png)

---

## Project Structure
```
Retail_dropoff_analysis/
├── data/                      # Raw and processed CSVs for analysis & dashboarding
│   ├── events.csv              # Main clickstream data
│   ├── item_properties_part1.csv
│   ├── item_properties_part2.csv
│   ├── category_tree.csv
│   └── kpi_data/               # Exported KPI summaries for Tableau
├── notebooks/
│   └── retail_root_cause_analysis_nb.ipynb
├── dashboards/
│   └── E-Commerce_Funnel_Insights.twb
├── reports/
|   ├── E-Commerce Funnel Insights Conversion Drop-Off Diagnostics.png
│   └── Final_Report.md             # Analyst-style findings & recommendations
├── src/
│   └── utils.py                # Kaggle API setup & CSV loading functions
└── README.md                   # Project documentation
```

---

## KPIs Tracked
- **Total Users**
- **Daily Active Users (DAU) & Monthly Active Users (MAU)**
- **Conversion Rate** (View -> Transaction)
- **Cart Abandonment Rate**
- **Click-to-Cart Rate**
- **Click-to-Purchase Rate**
- **Hourly Conversion Rate**
- **Average Session Depth**
- **Top 10 Items by Drop-off Count**
- **Category-wise Conversion Rate**

---

## Dashboard Features
- Funnel visualization showing user drop-off percentages
- Category-level leaders and laggers
- Top 10 drop off products
- Hourly conversion analysis
- DAU trends over the analysis period
- Interactive filters for category, date, and hour

---

## Tools & Technologies
- **Python**: pandas, matplotlib
- **Tableau**: Interactive dashboards, KPI cards, funnel visualization
- **Kaggle API**: Data import automation
- **Jupyter Notebook**: Data cleaning and transformation

---

## Key Insights
- Less than 1% of users who view a product complete a purchase.
- Cart abandonment rate is ~69%.
- Peak conversions occur in the evening (4–8 PM), with mornings underperforming.
- Certain categories have high conversion rates (>20%), while others are below 10%.
- A small number of products have high views and adds to cart but low purchases — key optimization targets.

---

## Data Workflow

1. **Data Acquisition**
   - Automated download from Kaggle using `utils.py` (retailrocket/ecommerce-dataset).
   - Loaded events.csv and supplementary item/category metadata.

2. **Exploratory Data Analysis**
   - Distribution of event types
   - Date range validation and timestamp parsing

3. **User Engagement Analysis**
   - DAU & MAU calculation and visualization
   - Session depth metrics

4. **Funnel Metrics**
   - From product view -> add to cart -> purchase
   - Drop-off analysis and rates

4. **Root Cause Exploration**
   - Hourly conversion trends
   - Category-level performance
   - Top high-drop-off items

5. **Export for Dashboarding**
   - Saved all KPI summaries (`kpi_data/*.csv`) for Tableau visualization.

---

## Contact
Created by Yatri Patel.
