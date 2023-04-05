import pytest

@pytest.fixture
def test_create_user():
    url = "http://127.0.0.1:8080/api/user"

    payload = {
        "id": 1,
        "email": "test@example.com",
        "password": "password",
        "role": "student"
    }

    response = requests.post(url, data=payload)

    # Assert that the request-response cycle completed successfully.
    assert response.status_code == 200

    # Assert that the response body is what we expect.
    assert response.json["email"] == "test@example.com"
    assert response.json["password"] == "password"
    assert response.json["role"] == "student"

if __name__ == "__main__":
    pytest.main()
