import streamlit as st
import pandas as pd
import numpy as np

st.title("AI-Based Battery Second-Life Optimisation")

st.write("EV Battery Health Analysis and Reuse Recommendation")

st.header("Enter Battery Details")

battery_capacity = st.number_input(
    "Original Battery Capacity (kWh)",
    min_value=1.0,
    value=60.0
)

remaining_capacity = st.number_input(
    "Current Battery Capacity (kWh)",
    min_value=0.1,
    value=48.0
)

battery_temperature = st.number_input(
    "Battery Temperature (°C)",
    value=30.0
)

electricity_cost = st.number_input(
    "Electricity Cost (₹ per kWh)",
    min_value=0.0,
    value=8.0
)

if st.button("Analyse Battery"):
    battery_health = (
        remaining_capacity / battery_capacity
    ) * 100

    st.subheader("Battery Analysis Results")

    st.write(
        "Estimated Battery Health:",
        round(battery_health, 2),
        "%"
    )

    if battery_health >= 80:
        st.success("Possible use: EV battery, subject to safety checks.")
    elif battery_health >= 60:
        st.info("Possible use: Stationary energy storage, after testing.")
    else:
        st.warning("Battery requires professional assessment.")

    if battery_temperature > 40:
        st.warning("High temperature. Check battery cooling and safety.")

