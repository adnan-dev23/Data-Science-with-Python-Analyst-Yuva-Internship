# Week 1: Data Science Orientation & Problem Definition in Beauty & Wellness

- **Track:** Data Science with Python Analyst[cite: 1]
- **Organization:** YuvaIntern (Henry Harvin Education)[cite: 2]
- **Author:** Adnan Shah Ashfaque Shah[cite: 1, 2]
- **Submission Date:** September 30, 2026[cite: 1]
- **Deliverable File:** [`Yuva_Internship_Week1_Report.docx`](Yuva_Internship_Week1_Report.docx)[cite: 1]

---

## 📌 Project Overview
This module defines the business problem, research scope, and analytical strategy to identify early churn indicators and repeat purchase drivers for a Direct-to-Consumer (D2C) skincare brand[cite: 1].

---

## 🎯 Business Problem Summary
- **Current Issue:** A mid-sized D2C skincare brand experiences a 55% to 60% customer churn within 90 days of the first purchase[cite: 1].
- **Core Objective:** Build an early-warning predictive system targeting at-risk users within 30 to 45 days post-delivery to reduce 90-day churn by 10% to 15%[cite: 1].

---

## 🔬 Research Hypotheses
- **Hypothesis 1:** Customers purchasing complete multi-step routine bundles exhibit at least a 25% higher 90-day retention rate compared to single-item buyers[cite: 1].
- **Hypothesis 2:** Inactivity on website tracking or store sessions within 21 days post-delivery correlates with over a 75% churn probability[cite: 1].
- **Hypothesis 3:** Customers acquired via deep discounts (>30%) exhibit a 40% lower 6-month Customer Lifetime Value (CLV)[cite: 1].

---

## 🛠️ Planned Methodology
1. **Data Ingestion & Cleaning:** Handle missing feedback ratings and audit transaction logs via pandas[cite: 1].
2. **Exploratory Data Analysis (EDA):** Cohort retention curves, product category performance, and discount sensitivity plots[cite: 1].
3. **Feature Engineering:** RFM scoring, bundle indicator flags (`is_bundle_buyer`), and categorical encoding[cite: 1].
4. **Predictive Modeling:** Train baseline Logistic Regression, Random Forest, and XGBoost classifiers with SMOTE for class imbalance[cite: 1].
5. **Evaluation & CRM Integration:** Optimize for Recall and ROC-AUC to translate model insights into automated CRM retention triggers[cite: 1].
