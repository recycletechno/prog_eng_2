# tests/test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_predict_sentiment(self):
        with app.test_client() as client:
            response = client.post('/predict', json={'text': 'This is a great movie!'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'sentiment': 'positive'})