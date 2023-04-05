# tests/test_app.py
import unittest
from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def get_test(get_client: TestClient):
    response = get_client.post('/predict', json={'text': 'This is a great movie!'})
    assert response.status_code == 200
    assert response.json == {'sentiment': 'positive'}