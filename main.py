from fastapi import FastAPI
from classifier import classify_site

app = FastAPI()

@app.get("/classify")
def classify(q: str):
    result = classify_site(q)
    return {"decision": result}
