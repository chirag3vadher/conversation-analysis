import pytest
import pandas as pd
from src.sentiment import analyze_sentiment, add_sentiment_column

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def test_analyze_sentiment():
    """Test sentiment classification."""
    test_cases = [
        ("I love this product!", "positive"),
        ("This is the worst experience ever.", "negative"),
        ("It's okay, I guess.", "neutral"),
        ("", "neutral"),
        (None, "neutral"),
    ]

    for text, expected in test_cases:
        score = sia.polarity_scores(text)["compound"] if text else 0
        predicted = analyze_sentiment(text)
        print(f"Text: {text}, Score: {score}, Predicted: {predicted}, Expected: {expected}")
        assert predicted == expected


@pytest.fixture
def sample_dataframe():
    """Creates a sample DataFrame for testing."""
    return pd.DataFrame({"message": ["I love this!", "Terrible service.", "It's fine."]})

def test_add_sentiment_column(sample_dataframe):
    """Test adding sentiment analysis to a DataFrame."""
    df = add_sentiment_column(sample_dataframe, "message")
    
    assert "sentiment" in df.columns
    assert df["sentiment"][0] == "positive"
    assert df["sentiment"][1] == "negative"
    assert df["sentiment"][2] == "neutral"
