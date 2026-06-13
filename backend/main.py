from fastapi import FastAPI
from pydantic import BaseModel
from utils.scraper import extract_text
from utils.predictor import predict_scores

app = FastAPI()

class RequestData(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "Fake News Detector API Running"}

@app.post("/predict")
def predict(data: RequestData):
    text = extract_text(data.url)
    
    if not text:
        return {"error": "Could not extract article text"}
    
    result = predict_scores(text)
    return result