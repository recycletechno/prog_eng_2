import unittest
from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_response():
    response = client.post('/predict', json={'text': 'Ekb is a great city!'})
    resp_json = response.json()

    assert response.status_code == 200
    assert isinstance(resp_json, dict), 'Response of wrong type!'

    if 'sentiment' in resp_json:
        assert resp_json['sentiment']['sentiment'] == 'POSITIVE'
    else:
        raise AssertionError('Sentiment key is not in dict')