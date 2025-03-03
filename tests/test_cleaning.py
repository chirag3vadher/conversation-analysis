import pytest
import pandas as pd
from src.cleaning import clean_text, clean_dataframe

def test_clean_text():
    """Test individual text cleaning."""
    assert clean_text("Hello!! How are you?") == "hello"
    assert clean_text("Price is $500.") == "price $500"
    assert clean_text("Call me at 123-456-7890.") == "call 123-456-7890"
    assert clean_text("Meeting on 03/03/2024.") == "meeting 03/03/2024"
    assert clean_text(None) == ""

@pytest.fixture
def sample_dataframe():
    """Creates a sample DataFrame for testing."""
    return pd.DataFrame({"message": ["Hello!!", "Price is $500.", "Meeting on 03/03/2024."]})

def test_clean_dataframe(sample_dataframe):
    """Test cleaning of a DataFrame column."""
    cleaned_df = clean_dataframe(sample_dataframe, "message")
    assert cleaned_df["message"][0] == "hello"
    assert cleaned_df["message"][1] == "price $500"
    assert cleaned_df["message"][2] == "meeting 03/03/2024"
