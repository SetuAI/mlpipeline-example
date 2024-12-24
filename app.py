import streamlit as st
import os
import numpy as np
import pandas as pd
from src.mlProject.pipeline.prediction import PredictionPipeline

st.title("Wine Quality Prediction")

if st.button("Train Model"):
    os.system("python main.py")  # Keep training separate
    st.success("Training Complete!")

with st.form("prediction_form"):
    st.header("Enter Wine Parameters:")
    fixed_acidity = st.number_input("Fixed Acidity", value=7.0)
    volatile_acidity = st.number_input("Volatile Acidity", value=0.5)
    citric_acid = st.number_input("Citric Acid", value=0.3)
    residual_sugar = st.number_input("Residual Sugar", value=2.0)
    chlorides = st.number_input("Chlorides", value=0.07)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=30.0)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=100.0)
    density = st.number_input("Density", value=0.995)
    pH = st.number_input("pH", value=3.2)
    sulphates = st.number_input("Sulphates", value=0.6)
    alcohol = st.number_input("Alcohol", value=10.0)

    submitted = st.form_submit_button("Predict")


    if submitted:  # Only make predictions when form submitted to avoid unnecessary calls
        try:
            data = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                             free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]).reshape(1, -1)
            obj = PredictionPipeline()
            prediction = obj.predict(data)

            if prediction is None:
                st.error("Prediction failed. Check your model and inputs.")
            else:
                st.success(f"Predicted Wine Quality: {prediction[0]}")  # Show prediction
        except Exception as e:
            st.error(f"An error occurred: {e}")