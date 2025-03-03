import pytest
import pandas as pd
from src.data_prep import load_data

# Define a test dataset (sample CSV content)
TEST_CSV_PATH = "tests/test_chat_sentiment.csv"
TEST_DATA = """message,sentiment
"Hello, how are you?",positive
"I'm not feeling great today.",negative
"Let's meet at 5 pm.",neutral
"""

@pytest.fixture
def setup_test_data():
    """Creates a temporary test CSV file."""
    with open(TEST_CSV_PATH, "w") as f:
        f.write(TEST_DATA)

def test_load_data(setup_test_data):
    """Test loading data from CSV."""
    df = load_data(TEST_CSV_PATH)
    
    # Check if DataFrame is not empty
    assert not df.empty, "Loaded DataFrame is empty"

    # Check if columns exist
    expected_columns = ["message", "sentiment"]
    assert list(df.columns) == expected_columns, "Unexpected column names"

    # Check the number of rows
    assert len(df) == 3, "Incorrect number of rows loaded"
