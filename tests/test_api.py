import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    """Test the root endpoint."""
    response = requests.get(BASE_URL + "/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sentiment Analysis API!"}

def test_analyze_text():
    """Test the sentiment analysis API."""
    response = requests.post(
        BASE_URL + "/analyze/",
        json={"text": "This is amazing!"}
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"
