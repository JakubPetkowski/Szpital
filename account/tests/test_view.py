from django.urls import reverse
import pytest
from django.test import Client


@pytest.fixture

def client():
    client = Client()
    return client


def test_home(client):
    response = client.get('/account/home/')
    assert response.status_code == 200


def test_aboutus(client):
    response = client.get('/account/aboutus/')
    assert response.status_code == 302


def test_contact(client):
    response = client.get('/account/contact.html/')
    assert response.status_code == 302


def test_SignUp(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    # client.login(username=username, password=password)
    response = client.get('/account/signup/')
    assert response.status_code == 200


def test_updated_user_profile_view(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    # client.login(username=username, password=password)
    response = client.get('//')
    assert response.status_code == 200


