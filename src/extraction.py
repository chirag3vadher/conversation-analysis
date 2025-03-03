import pandas as pd

def extract_utterances(data: pd.DataFrame) -> tuple:
    """
    Extracts agent and customer utterances from the chat data.
    
    Args:
        data (pd.DataFrame): DataFrame with 'speaker' and 'message' columns.
        
    Returns:
        tuple: Two lists - (agent_utterances, customer_utterances)
    """
    if "speaker" not in data.columns or "message" not in data.columns:
        raise ValueError("Data must contain 'speaker' and 'message' columns.")

    agent_utterances = data[data["speaker"] == "Agent"]["message"].tolist()
    customer_utterances = data[data["speaker"] == "Customer"]["message"].tolist()

    return agent_utterances, customer_utterances
