import pandas as pd
from src.data_prep import load_data
from src.cleaning import clean_dataframe
from src.sentiment import add_sentiment_column

def process_pipeline(input_file: str, text_column: str, output_file: str):
    """
    Full pipeline: Load data → Clean text → Perform sentiment analysis → Save results.
    
    Args:
        input_file (str): Path to the input CSV file.
        text_column (str): Column containing text data.
        output_file (str): Path to save the processed results.
    """
    # Step 1: Load data
    data = load_data(input_file)

    # Step 2: Clean text
    data = clean_dataframe(data, text_column)

    # Step 3: Perform sentiment analysis
    data = add_sentiment_column(data, text_column)

    # Step 4: Save processed data
    data.to_csv(output_file, index=False)
    print(f"Processed data saved to: {output_file}")

if __name__ == "__main__":
    # Example usage
    process_pipeline("data/raw/conversations.csv", "message", "data/processed/processed_data.csv")
