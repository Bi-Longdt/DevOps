import pytest
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, read_categortys, read_products

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Clean up the test data after testing
    yield client

def test_secure_password_hashing():
    # Test if the password hashing functions are secure
    password = "secret_password"
    hashed_password = generate_password_hash(password)
    assert check_password_hash(hashed_password, password)
    assert not check_password_hash(hashed_password, "wrong_password")

def test_categorty_data_privacy(client: FlaskClient):
    # Test if the category data is not exposed to unauthorized users
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    content_text = soup.get_text()

    # Now check if 'categorty' is present only in the HTML content
    assert 'categorty' not in content_text

def test_product_data_privacy(client: FlaskClient):
    # Test if the product data is not exposed to unauthorized users
    response = client.get('/')
    assert b'products' not in response.data

# def test_secure_file_uploads():
    # Test if file uploads are secure
    # You may need to mock file upload functionality for this test

    # Example:
    # with app.test_request_context('/'):
    #     # Simulate a file upload
    #     file_data = {
    #         'product_image': (BytesIO(b'my_file_content'), 'example.jpg')
    #     }
    #     response = app.test_client().post('/add_product', data={'key': 'value'}, files=file_data)
    #
    # assert b'File uploaded successfully' in response.data
    # ...

# Add more security tests based on your specific security requirements