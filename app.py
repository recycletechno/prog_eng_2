from fastapi import FastAPI
from pydantic import BaseModel
from get_sentiment import get_sentiment_fx
import uvicorn

app = FastAPI()


class InputText(BaseModel):
    text: str


# Add a simple GET response at the base url "/"
@app.get("/")
def read_root():
    return {"test_response": "Hello URFU World!"}


@app.post("/predict")
async def predict_sentiment(input_text: InputText):
    sentiment = get_sentiment_fx(input_text.text)
    return {
        "text": input_text.text,
        "sentiment": sentiment,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info")
