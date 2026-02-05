# Ride Price Estimation System

## Project Overview
This project demonstrates an end-to-end machine learning workflow for estimating ride
prices using synthetic data. The focus is on ML reasoning, dataset design, preprocessing,
modeling, evaluation, and ethical reflection.

## Dataset Description
The dataset was synthetically generated with over 200 rows and includes both numerical and
categorical features. The target variable is a continuous ride price.

The dataset intentionally includes duplicates, outliers, impossible values, and inconsistent
labels to simulate real-world data quality issues.

## Features Used
- distance (km)
- duration (minutes)
- traffic (categorical)
- weather (categorical)
- time_of_day (categorical)
- demand (categorical)
- price (target)

## Data Cleaning
- Removed duplicates
- Fixed categorical inconsistencies
- Handled outliers and impossible values
- Encoded categorical variables
- Scaled numerical features

## Models Used
- Linear Regression for price prediction
- Logistic Regression for high-cost vs low-cost classification

## Key Findings
- Data quality significantly impacts model performance
- Linear regression captures pricing trends but is sensitive to outliers
- Classification simplifies interpretation but reduces precision

## How to Run
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```
3. Open `notebook/ride_price_model.ipynb`
4. Run cells sequentially using VS Code or Google Colab

## Ethical Reflection
The model may unintentionally promote unfair pricing if demand-based features are misused.
Synthetic data also limits real-world generalization.
