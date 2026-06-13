from model_loader import model, vectorizer
from utils.preprocess import clean_text

def predict_scores(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    
    fake_score = model.predict_proba(vec)[0][1]
    
    # Placeholder for AI-generated detection
    ai_score = fake_score * 0.8  # replace later
    
    return {
        "fake_score": float(fake_score),
        "ai_generated_score": float(ai_score)
    }