from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse, resolve
from mixer.backend.django import mixer
import pytest
from django.test import TestCase


@pytest.mark.django_db
class TestViews(TestCase):

    def test_signup_get_succeess(self):
        path = reverse('signup')
        request = RequestFactory().get(path)

        response = self.client.get(path)
        assert response.status_code == 200

    def test_signup_post_succeess(self):
        path = reverse('signup')
        request = RequestFactory().post(path)

        data = {
            'username': 'Amit',
            'password': 'amit',
            'repassword': 'amit'
        }
        response = self.client.post(path, data=data)
        assert response.url == '/'

    def test_signup_username_blank(self):
        path = reverse('signup')
        request = RequestFactory().post(path)

        data = {
            'username': '',
            'password': 'amit',
            'repassword': 'amit'
        }
        response = self.client.post(path, data=data)
        assert response.status_code == 200

    def test_signup_password_mismatch(self):
        path = reverse('signup')
        request = RequestFactory().post(path)

        data = {
            'username': '',
            'password': 'amit',
            'repassword': 'a'
        }
        response = self.client.post(path, data=data)
        assert response.status_code == 200

    def test_login_get_success(self):
        path = reverse('login')
        request = RequestFactory().get(path)

        response = self.client.get(path)
        assert response.status_code == 200

    def test_login_post_success(self):
        path = reverse('login')
        request = RequestFactory().post(path)

        data = {
            'username': 'Amit Singh',
            'password': 'amit',
            'repassword': 'a'
        }
        response = self.client.post(path, data=data)
        assert response.status_code == 200

    def test_logout_success(self):
        path = reverse('logout')
        request = RequestFactory().post(path)

        response = self.client.post(path)
        assert response.url == '/'
