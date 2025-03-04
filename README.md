# 📝 Conversation Sentiment Analysis  
🚀 A modular **NLP project** for analyzing sentiment in conversations.  
Includes **FastAPI**, **Streamlit Dashboard**, and **Docker** for easy deployment.  

---

## 📌 Features  
✅ Extracts customer & agent utterances  
✅ Cleans text while preserving numbers (e.g., `$500`, `₹2000`)  
✅ Performs **sentiment analysis** using VADER  
✅ Provides **FastAPI** for real-time sentiment analysis  
✅ Offers a **Streamlit dashboard** for CSV uploads & visualizations  
✅ Fully containerized using **Docker**  

---

## 📌 Project Structure  
```
📂 conversation-analysis  
│── 📂 api                 # FastAPI backend  
│   └── main.py            # API for sentiment analysis  
│  
│── 📂 src                 # Core modules  
│   ├── data_prep.py       # Load & preprocess data  
│   ├── cleaning.py        # Clean conversation text  
│   ├── sentiment.py       # Perform sentiment analysis  
│   ├── pipeline.py        # Full processing pipeline  
│  
│── 📂 tests               # Unit tests  
│   ├── test_cleaning.py   # Test text cleaning  
│   ├── test_sentiment.py  # Test sentiment analysis  
│   ├── test_pipeline.py   # Test end-to-end pipeline  
│   ├── test_api.py        # Test API endpoints  
│  
│── app.py                 # Streamlit dashboard  
│── Dockerfile             # Docker container setup  
│── requirements.txt       # Dependencies  
│── README.md              # Project documentation  
```

---

## 📌 Installation & Setup  
### 1️⃣ Clone the Repository  
```bash  
git clone https://github.com/chirag3vadher/conversation-analysis.git  
cd conversation-analysis  
```  

### 2️⃣ Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### 3️⃣ Run FastAPI API  
```bash  
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload  
```  
- Visit **http://127.0.0.1:8000/docs** for API documentation.  

### 4️⃣ Run Streamlit Dashboard  
```bash  
streamlit run app.py  
```  
- Open **http://localhost:8501** to upload CSV files and visualize sentiment.  

---  

## 📌 Run with Docker  
### 1️⃣ Build Docker Image  
```bash  
docker build -t sentiment-analysis .  
```  
### 2️⃣ Run Container  
```bash  
docker run -p 8000:8000 -p 8501:8501 sentiment-analysis  
```  
- API → **http://localhost:8000**  
- Dashboard → **http://localhost:8501**  

---  

## 📌 Running Tests  
Run all unit tests using `pytest`:  
```bash  
pytest tests/  
```  

---  

## 📌 Example API Request  
Use `curl` to test the API:  
```bash  
curl -X 'POST' 'http://127.0.0.1:8000/analyze/' \  
-H 'Content-Type: application/json' \  
-d '{"text": "I love this product!"}'  
```  
✅ **Expected Response:**  
```json  
{"text": "I love this product!", "sentiment": "positive"}  
```  
---  

### 🔥 Now you’re all set!  
