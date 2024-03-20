import pytest


@pytest.mark.django_db
def test_register_user_failure(client):
    url = '/v1/users/register/'
    user_data = {
        "email": "test@email.com",
        "name": "tester",
        "password": "12345678",
        "password_confirmation": "12345678"
    }
    response = client.post(url, user_data, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_user_success(client):
    url = '/v1/users/register/'
    user_data = {
        "email": "test@email.com",
        "name": "tester",
        "password": "12345678A@",
        "password_confirmation": "12345678A@"
    }
    response = client.post(url, user_data, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_login_user_success(client, user_factory):
    user_password = "12345678A@"
    user = user_factory.create(email='user@test.com')
    user.set_password(user_password)
    user.save()
    url = '/v1/users/login/'
    payload = {"email": user.email, "password": user_password}
    response = client.post(url, payload, format='json')
    
    assert response.status_code == 200

