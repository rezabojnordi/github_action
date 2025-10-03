# This file contains automated tests for the Flask application using pytest.
# These tests run in the CI/CD pipeline to ensure code quality before deployment.

from app import app
import pytest

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world_endpoint(client):
    """
    Test the main endpoint ('/').
    It should return a 200 OK status and the correct greeting message.
    """
    # GIVEN a test client
    # WHEN a GET request is made to the root URL
    response = client.get('/')
    
    # THEN the response should be successful and contain the expected text
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
