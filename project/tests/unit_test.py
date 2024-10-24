import pytest
from application import application
import json

@pytest.fixture
def client():
    with application.app_context():
        yield application.test_client()

def test_real_1(client):
    # Test case 1 for real news prediction
    response = client.post('/predict', data=json.dumps({"text": "Poutine comes from Quebec."}),
                           content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['prediction'] == 'REAL'  # Expected output for real news

def test_real_2(client):
    # Test case 2 for real news prediction
    response = client.post('/predict', data=json.dumps({"text": "Montreal is a better city than Toronto"}),
                           content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['prediction'] == 'REAL'  # Expected output for real news

def test_fake_1(client):
    # Test case 1 for fake news prediction
    response = client.post('/predict', data=json.dumps({"text": "The earth is flat"}),
                           content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['prediction'] == 'FAKE'  # Expected output for fake news

def test_fake_2(client):
    # Test case 2 for fake news prediction
    response = client.post('/predict', data=json.dumps({"text": "COVID-19 is a hoax"}),
                           content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['prediction'] == 'FAKE'  # Expected output for fake news