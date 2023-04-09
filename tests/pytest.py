import pytest
import requests

# @pytest.fixture
def test_create_user():
    url = "http://0.0.0.0:8080/api/user"

    payload = {
        "email": "test@example.com",
        "password": "password",
        "role": "student"
    }


    response = requests.post(url, data=payload)
    print(response.text)

    # Assert that the request-response cycle completed successfully.
    assert response.status_code == 200

    # Assert that the response body is what we expect.
    assert response.json["email"] == "test@example.com"
    assert response.json["password"] == "password"
    assert response.json["role"] == "student"

if __name__ == "__main__":
    test_create_user()
