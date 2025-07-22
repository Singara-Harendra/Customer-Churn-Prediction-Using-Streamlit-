# 📉 Customer-Churn-Prediction-Using-Streamlit-

A machine learning-powered web application built using **Streamlit** that predicts whether a customer is likely to churn based on inputs like age, tenure, gender, monthly charges, and tech support availability.

---

## 🔍 Features

- Loads and processes customer data (`customer_churn_data.csv`)
- Performs:
  - Missing value handling
  - Encoding of categorical variables
  - Feature scaling with `StandardScaler`
- Trains and evaluates multiple ML models:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Decision Tree
  - Random Forest
- Uses `GridSearchCV` for hyperparameter tuning
- Saves the best model and scaler using `joblib`
- Deploys prediction interface using **Streamlit**

---

## 🧪 Input Features

| Feature         | Description                          |
|----------------|--------------------------------------|
| `Age`          | Age of the customer                  |
| `Gender`       | Male / Female                        |
| `Tenure`       | Duration (in months) with the company|
| `MonthlyCharges` | Monthly payment amount              |
| `TechSupport`  | Whether customer has tech support    |

---



