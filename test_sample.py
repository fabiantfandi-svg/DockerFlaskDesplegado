import pytest
from sample_app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_read_main_success(client):
    """Valida que la ruta principal devuelva un código HTTP 200 OK."""
    response = client.get('/')
    assert response.status_code == 200
    
# def test_ejemplo_basico():
 # assert 1 + 1 == 2