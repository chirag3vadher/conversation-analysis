import re
import pandas as pd
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download("stopwords")

def clean_text(text: str) -> str:
    """
    Cleans text while preserving numerical values.
    
    Args:
        text (str): The input text message.
        
    Returns:
        str: The cleaned text.
    """
    if not isinstance(text, str):
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove special characters but keep numbers, currencies, and slashes for dates
    text = re.sub(r"[^\w\s\$\%\/-]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Remove stopwords (excluding numbers)
    words = text.split()
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words or word.isnumeric()]
    
    return " ".join(filtered_words)


def clean_dataframe(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Applies text cleaning to a specified column in a DataFrame.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        column (str): The column containing text to clean.
        
    Returns:
        pd.DataFrame: The DataFrame with cleaned text.
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    
    data[column] = data[column].apply(clean_text)
    return data
