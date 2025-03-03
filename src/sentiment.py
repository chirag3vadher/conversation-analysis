import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize VADER
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> str:
    """
    Classifies text sentiment as positive, negative, or neutral.
    
    Args:
        text (str): The input text.
        
    Returns:
        str: "positive", "negative", or "neutral".
    """
    if not isinstance(text, str) or text.strip() == "":
        return "neutral"

    score = sia.polarity_scores(text)["compound"]

    if score >= 0.25:
        return "positive"
    elif score <= -0.25:
        return "negative"
    else:
        return "neutral"

def add_sentiment_column(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Adds a sentiment column to a DataFrame.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        column (str): The text column to analyze.
        
    Returns:
        pd.DataFrame: DataFrame with an added 'sentiment' column.
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    
    data["sentiment"] = data[column].apply(analyze_sentiment)
    return data
