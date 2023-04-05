# Sentiment Analysis Application

This is a small machine learning application for sentiment analysis that uses a pre-trained model from Hugging Face's Transformers library. The application is implemented in Python and uses the Flask web framework for serving predictions.

## Installation

To install the required dependencies, you can use the following command:


```shell
pip install -r requirements.txt
```

## Usage

To start the Flask app, run the following command:

```shell
flask run
```

This should start the app and make it available at http://localhost:5000.

To send a POST request to the `/predict` endpoint, you can use `curl` or an HTTP client like Postman. For example, you can use the following `curl` command:

```shell
curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "I love this product!"
}'
```

This should return a JSON response with the predicted sentiment:

```json
{"sentiment": "POSITIVE"}
```

You can test other input texts as well to see how the model performs.

When you're finished testing, you can stop the Flask app by pressing Ctrl+C in the terminal.

## Dependencies

The application requires the following Python packages:

flask
transformers
flake8