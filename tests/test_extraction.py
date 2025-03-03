import pytest
import pandas as pd
from src.extraction import extract_utterances

@pytest.fixture
def sample_data():
    """Provides a sample DataFrame for testing."""
    return pd.DataFrame({
        "speaker": ["Agent", "Customer", "Agent", "Customer"],
        "message": [
            "Hello, how can I help you?",
            "I need help with my order.",
            "Sure, what's the issue?",
            "I received the wrong item."
        ]
    })

def test_extract_utterances(sample_data):
    """Test that utterances are correctly extracted."""
    agent_utts, customer_utts = extract_utterances(sample_data)

    assert agent_utts == ["Hello, how can I help you?", "Sure, what's the issue?"]
    assert customer_utts == ["I need help with my order.", "I received the wrong item."]
