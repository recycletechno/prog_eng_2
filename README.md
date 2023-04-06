# Sentiment Analysis Application

This is a small machine learning application for sentiment analysis that uses a pre-trained model. The application is implemented in Python and uses the FastAPI framework for serving predictions.

## Installation

To install the required dependencies, you can use the following command:


```shell
pip install -r requirements.txt
```

## Usage

To start the app, run the following command:

```shell
python app.py
```

This should start the app and make it available at http://localhost:8080.

To send a POST request to the `/predict` endpoint, you can use `curl` or an HTTP client like Postman. For example, you can use the following `curl` command:

```shell
curl --location --request POST "http://localhost:5000/predict" \
--header "Content-Type: application/json" \
--data-raw "{
    \"text\": \"I love EKB!\"
}"
```

This should return a JSON response with the predicted sentiment:

```json
{"text":"I love EKB!","sentiment":{"sentiment":"POSITIVE","polarity":0.9985707998275757}}
```

You can test other input texts as well to see how the model performs.

When you're finished testing, you can stop the FastAPI app (uvicorn server) by pressing Ctrl+C in the terminal.

## Dependencies

The application requires the following Python packages:

- httpx
- fastapi
- uvicorn
- pydantic
- flake8
- flair