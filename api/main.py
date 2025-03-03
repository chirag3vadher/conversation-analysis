from fastapi import FastAPI
from pydantic import BaseModel
from src.sentiment import analyze_sentiment

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze/")
def analyze_text(input_data: TextInput):
    """
    Endpoint to analyze sentiment of a given text.
    """
    sentiment = analyze_sentiment(input_data.text)
    return {"text": input_data.text, "sentiment": sentiment}

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API!"}
