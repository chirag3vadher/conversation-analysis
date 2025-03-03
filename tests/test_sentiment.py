import pytest
import pandas as pd
from src.sentiment import analyze_sentiment, add_sentiment_column

def test_analyze_sentiment():
    """Test sentiment classification."""
    assert analyze_sentiment("I love this product!") == "positive"
    assert analyze_sentiment("This is the worst experience ever.") == "negative"
    assert analyze_sentiment("It's okay, I guess.") == "neutral"
    assert analyze_sentiment("") == "neutral"
    assert analyze_sentiment(None) == "neutral"

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
