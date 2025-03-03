import os
import pandas as pd
from src.pipeline import process_pipeline

def test_pipeline():
    """Test the full pipeline."""
    input_file = "data/raw/sample.csv"
    output_file = "data/processed/sample_output.csv"

    # Create a small sample dataset
    sample_data = pd.DataFrame({"message": ["I love it!", "Worst experience ever.", "It's okay."]})
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    sample_data.to_csv(input_file, index=False)

    # Run pipeline
    process_pipeline(input_file, "message", output_file)

    # Check output
    assert os.path.exists(output_file), "Output file was not created."
    
    df = pd.read_csv(output_file)
    assert "sentiment" in df.columns, "Sentiment column missing."
    assert df["sentiment"][0] == "positive"
    assert df["sentiment"][1] == "negative"
    assert df["sentiment"][2] == "neutral"

    # Cleanup
    os.remove(input_file)
    os.remove(output_file)
