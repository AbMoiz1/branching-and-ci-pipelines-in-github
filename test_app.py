import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret_key'
    with app.test_client() as client:
        yield client


def test_home_redirects_to_login(client):
    """Test that home page redirects to login when not authenticated."""
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.location


def test_login_page_loads(client):
    """Test that login page loads successfully."""
    response = client.get('/login')
    assert response.status_code == 200


def test_login_with_valid_credentials(client):
    """Test login with correct credentials."""
    response = client.post('/login', data={
        'username': 'admin',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_login_with_invalid_credentials(client):
    """Test login with incorrect credentials."""
    response = client.post('/login', data={
        'username': 'wrong',
        'password': 'wrong'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_welcome_requires_login(client):
    """Test that welcome page requires authentication."""
    response = client.get('/welcome')
    assert response.status_code == 302
    assert '/login' in response.location


def test_logout(client):
    """Test logout functionality."""
    # First login
    client.post('/login', data={
        'username': 'admin',
        'password': 'password123'
    })
    # Then logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
