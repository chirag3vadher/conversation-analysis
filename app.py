import streamlit as st
import pandas as pd
from src.pipeline import process_pipeline

st.title("📊 Conversation Sentiment Analysis")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Save uploaded file
    input_path = "data/raw/uploaded.csv"
    output_path = "data/processed/processed_data.csv"
    
    df = pd.read_csv(uploaded_file)
    df.to_csv(input_path, index=False)
    
    st.write("### Preview of Uploaded Data")
    st.write(df.head())

    # Process pipeline
    st.write("🚀 Running sentiment analysis...")
    process_pipeline(input_path, "message", output_path)

    # Show results
    processed_df = pd.read_csv(output_path)
    st.write("### Sentiment Analysis Results")
    st.write(processed_df.head())

    # Sentiment distribution
    st.write("### Sentiment Distribution")
    st.bar_chart(processed_df["sentiment"].value_counts())
