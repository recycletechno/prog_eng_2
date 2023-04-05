from transformers import pipeline

classifier = pipeline('sentiment-analysis')

def predict_sentiment(text):
    result = classifier(text)[0]
    label = result['label']
    return label
