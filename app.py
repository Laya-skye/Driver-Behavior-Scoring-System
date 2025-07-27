import streamlit as st
import pandas as pd

def calculate_driver_score(df):
    overspeed = (df['speed'] > 80).sum()
    brakes = (df['brake'] > 0.5).sum()
    accel = (df['acceleration'] > 0.5).sum()

    score = 100 - overspeed * 3 - brakes * 2 - accel * 1.5
    score = max(score, 0)
    return score, overspeed, brakes, accel

# Streamlit app
st.title("Driver Behavior Scoring System")
st.write("Upload a CSV file with `speed`, `acceleration`, and `brake` columns to calculate the driver score.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    score, ospeed, brakes, accel = calculate_driver_score(df)
    
    st.metric("Driver Score", f"{score:.2f}/100")
    st.write(f"**Overspeed Events:** {ospeed}")
    st.write(f"**Harsh Brakes:** {brakes}")
    st.write(f"**Sudden Accelerations:** {accel}")
    
    st.bar_chart(df[['speed', 'acceleration', 'brake']])
