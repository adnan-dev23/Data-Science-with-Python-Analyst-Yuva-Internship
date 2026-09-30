"""
Beauty & Wellness Customer Churn Analytics
Author: Adnan Shah Ashfaque Shah
Internship: Yuva Internship - Data Science with Python Analyst
"""

import pandas as pd
import numpy as np

def generate_sample_customer_data(n_samples=500):
    np.random.seed(42)
    categories = ['Serum', 'Cleanser', 'Moisturizer', 'Sunscreen', 'Kit/Bundle']
    channels = ['Meta Ads', 'Google Search', 'Influencer', 'Organic']
    
    data = {
        'customer_id': [f'CUST_{1000 + i}' for i in range(n_samples)],
        'acquisition_channel': np.random.choice(channels, size=n_samples, p=[0.4, 0.3, 0.2, 0.1]),
        'first_product_category': np.random.choice(categories, size=n_samples, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
        'initial_order_value': np.round(np.random.uniform(399, 2499, size=n_samples), 2),
        'initial_discount_pct': np.random.choice([0.0, 0.10, 0.15, 0.25, 0.35], size=n_samples),
        'site_sessions_30d': np.random.poisson(lam=3, size=n_samples),
        'post_delivery_rating': np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.05, 0.1, 0.15, 0.4, 0.3]),
        'churn_status': np.random.choice([0, 1], size=n_samples, p=[0.42, 0.58])
    }
    return pd.DataFrame(data)

def perform_eda_summary(df):
    print("==========================================")
    print("   BEAUTY & WELLNESS CHURN DATA SUMMARY   ")
    print("==========================================")
    print(f"Total Customer Records: {len(df)}")
    print(f"Overall Churn Rate: {df['churn_status'].mean() * 100:.2f}%")
    print("\n--- Churn Rate by Initial Product Category ---")
    category_churn = df.groupby('first_product_category')['churn_status'].mean() * 100
    print(category_churn.round(2).to_string())
    print("\n--- Average Order Value by Acquisition Channel ---")
    channel_aov = df.groupby('acquisition_channel')['initial_order_value'].mean()
    print(channel_aov.round(2).to_string())

if __name__ == "__main__":
    df = generate_sample_customer_data()
    perform_eda_summary(df)
