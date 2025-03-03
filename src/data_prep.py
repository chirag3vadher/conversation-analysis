import pandas as pd
import os

def load_data(file_path):
    """Loads the dataset from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"Dataset loaded successfully: {file_path}")
    print("\nPreview:")
    print(df.head())
    return df

def preprocess_data(df):
    """Handles missing values and basic cleaning."""
    print("\nChecking for missing values...")
    missing_counts = df.isnull().sum()
    print(missing_counts[missing_counts > 0])
    
    df = df.dropna().reset_index(drop=True)
    print("Missing values handled.")
    
    return df

if __name__ == "__main__":
    file_path = "data/raw/chat_sentiment.csv"  # Update if needed
    df = load_data(file_path)
    df = preprocess_data(df)
    
    output_path = "data/processed/cleaned_chat_sentiment.csv"
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to: {output_path}")
