# Week 1: Data Science Orientation & Problem Definition in Beauty & Wellness

- **Track:** Data Science with Python Analyst
- **Organization:** YuvaIntern (Henry Harvin Education)
- **Author:** Adnan Shah Ashfaque Shah
- **Submission Date:** September 30, 2026
- **Deliverable File:** (Yuva_Internship_Week1_Report.docx)

---

##  Project Overview
This module defines the business problem, research scope, and analytical strategy to identify early churn indicators and repeat purchase drivers for a Direct-to-Consumer (D2C) skincare brand.

---

##  Business Problem Summary
- **Current Issue:** A mid-sized D2C skincare brand experiences a 55% to 60% customer churn within 90 days of the first purchase.
- **Core Objective:** Build an early-warning predictive system targeting at-risk users within 30 to 45 days post-delivery to reduce 90-day churn by 10% to 15%.

---

##  Research Hypotheses
- **Hypothesis 1:** Customers purchasing complete multi-step routine bundles exhibit at least a 25% higher 90-day retention rate compared to single-item buyers.
- **Hypothesis 2:** Inactivity on website tracking or store sessions within 21 days post-delivery correlates with over a 75% churn probability.
- **Hypothesis 3:** Customers acquired via deep discounts (>30%) exhibit a 40% lower 6-month Customer Lifetime Value (CLV).

---

##  Planned Methodology
1. **Data Ingestion & Cleaning:** Handle missing feedback ratings and audit transaction logs via pandas.
2. **Exploratory Data Analysis (EDA):** Cohort retention curves, product category performance, and discount sensitivity plots.
3. **Feature Engineering:** RFM scoring, bundle indicator flags (`is_bundle_buyer`), and categorical encoding.
4. **Predictive Modeling:** Train baseline Logistic Regression, Random Forest, and XGBoost classifiers with SMOTE for class imbalance.
5. **Evaluation & CRM Integration:** Optimize for Recall and ROC-AUC to translate model insights into automated CRM retention triggers.
