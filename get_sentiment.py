from flair.models import TextClassifier
from flair.data import Sentence

sentiment_model = TextClassifier.load('en-sentiment')


def get_sentiment_dict(text: str) -> dict:
    """Parse a string, and determine sentiment polarity"""
    sentence = Sentence(text)
    sentiment_model.predict(sentence)
    label = sentence.labels[0]
    sentiment = {'sentiment': label.value, 'polarity': label.score}
    return sentiment


# Run a small test
if __name__ == '__main__':
    # We're testing if our sentiment and entity function is working correctly:
    result = get_sentiment_dict("I travelled to Eburg and I loved it.")
    print(result)
