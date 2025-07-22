import streamlit as st
import numpy as np
import joblib

scaler=joblib.load("scaler.pkl")
model=joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()

age = st.number_input("Enter age",min_value=10,max_value=100, value=30)

tenure=st.number_input("Enter the tenure",min_value= 0, max_value= 130, value=100)

monthlycharge= st.number_input("Enter the monthly charge",min_value=30, max_value=150)

gender = st.selectbox("Enter the Gender",["Male","Female"])

TechSupport= st.selectbox("Enter support",["Yes","No"])

st.divider()

predictbutton = st.button("Predict")

if predictbutton:

    gender_selected = 1 if gender == "Female" else 0

    TechSupport_selected = 1 if TechSupport == "Yes" else 0

    X = [age, gender_selected, tenure, monthlycharge, TechSupport_selected]

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    predicted = model.predict(X_array)[0]

    predicted = "YES" if predicted==1 else "NO"

    st.balloons()

    st.write(f"Predicted: {predicted}") 

else:
    st.write("Please enter the details and use the predict button")
